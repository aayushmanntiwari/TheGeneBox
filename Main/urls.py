"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Home.views import addauthors,addbooks,load_authors,create_table,show_name,csv_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls'),name="Home"),
    path('addauthor/',addauthors,name="addauthors"),
    path('addbook/',addbooks,name="addbooks"),
    path('ajax/load-authors/', load_authors, name='ajax_load_cities'),
    path('ajax/load-table/',create_table,name="create_table"),
    path('sayhi/<str:name>/',show_name,name='show_name'),
    path('create/csv/',csv_create,name="csv_create"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)