from django.db import models
from django.forms import ModelForm, Textarea

class Students(models.Model):
	username=models.CharField(max_length=255)
	keywords=models.CharField(max_length=255)
	Size=models.IntegerField()
	max_urls=models.IntegerField()



class Meta:
 db_table="students"	




class Scraping(models.Model):
   username=models.CharField(max_length=255)
   keywords=models.TextField(max_length=20)
   title=models.TextField()
   description=models.TextField()
   telephone=models.TextField()
   email=models.TextField()




class Meta:
 db_table="Scraping"
# Create your models here.








