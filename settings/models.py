from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class Setting(models.Model):
    title= models.CharField(max_length=200)
    about_description= models.TextField(blank=True)
    seo_keywords= models.TextField(blank=True)
    phone= models.CharField(max_length=20,blank=True)
    email= models.CharField(max_length=50,blank=True)
    facbook= models.CharField(max_length=50,blank=True)
    instagram= models.CharField(max_length=50,blank=True)
    twitter= models.CharField(max_length=50,blank=True)
    theme_color= ColorField(default='#FF0000',blank=True)
    logo=models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title







    



