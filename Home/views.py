import requests
import pycountry
import os
import csv
import pandas as pd
from django.shortcuts import render,redirect
from django.http import *
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import *
from rest_framework.response import Response
from .models import Authors,Books
from .serializers import AuthorsSerializers,BooksSerializers
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.


@api_view(['GET','POST'])
def home(request):
    return render(request,'index.html')


#code for adding authors 
@api_view(['POST'])
def addauthors(request):
    addauthorserializers = AuthorsSerializers(data = request.data)
    if addauthorserializers.is_valid():
        #addauthorserializers.save(user = request.user)
        addauthorserializers.save()
        return Response(addauthorserializers.data)
    return addauthorserializers(addauthorserializers.errors)


#code for adding books
@api_view(['POST'])
def addbooks(request):
    addbookserializers = BooksSerializers(data = request.data)
    if addbookserializers.is_valid():
        addbookserializers.save()
        return Response(addbookserializers.data)
    return addbookserializers(addbookserializers.errors)


#this code is called when we want to add books author ,so it will show all the authors names list without page load
@api_view(['GET'])
def load_authors(request):
    authors = Authors.objects.all()
    context = {
        'authors':authors,
    } 
    data = {'rendered_table': render_to_string('authors_dropdown_list_options.html',context=context)}
    return JsonResponse(data)


#this code will create the table
@api_view(['GET'])
def create_table(request):
    authors = Authors.objects.all()
    books = Books.objects.all()
    context = {
        'authors':authors,
        'books':books,
    } 
    data = {'rendered_table': render_to_string('table-create.html',context=context)}
    return JsonResponse(data)

#this method is called when we pass the name in the url.
@api_view(['GET'])
def show_name(request,name):
    messages.info(request,f"hello {name}")
    return redirect('/')

#this code will show create csv file .
@api_view(['GET'])
def csv_create(request):
    df = pd.read_csv(r'chrons_taxanomic_profile (1).tsv', sep='\t')
    output = df[df['#SampleID'].str.contains('t__')]
    output.to_csv('output.csv',index=False,header=True)
    data = pd.read_csv("output.csv")
    for row in data['#SampleID']:
        if 's__' in row:
            curr_row = str(row).split('|')
            for curr_val in curr_row:
                if 's__' in curr_val:
                    curr_row[curr_row.index(curr_val)]+='_pseudocatenulatum'
            data.replace(to_replace =row, value = '|'.join(curr_row),inplace = True)
    data.to_csv("output.csv")
    messages.info(request,"operation done")
    return redirect('/')


