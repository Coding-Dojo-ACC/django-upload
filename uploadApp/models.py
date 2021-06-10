from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Zoo(models.Model):
    zooName=models.CharField(max_length=45)
