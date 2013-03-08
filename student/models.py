from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=15)
    age = models.CharField(max_length=10)
    mark = models.CharField(max_length=15)
   
    

