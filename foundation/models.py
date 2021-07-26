from django.db import models

# Create your models here.

class data(models.Model):
    classname= models.CharField(max_length=10)
    subjectname= models.CharField(max_length=250)
    pdf= models.FileField(upload_to='pdfs')
    video= models.URLField()
    