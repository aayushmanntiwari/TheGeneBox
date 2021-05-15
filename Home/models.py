from django.db import models

# Create your models here.
class Authors(models.Model):
    first_name = models.CharField(max_length=100,blank=False,null=False)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.first_name + self.last_name
        return self.first_name
        

class Books(models.Model):
    book_name =  models.CharField(max_length=225,blank=False,null=False)
    book_genre = models.CharField(max_length=225,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)


    def __str__(self):
        return self.book_name
