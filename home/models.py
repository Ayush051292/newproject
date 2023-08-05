from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class home(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    dob=models.DateField()

class emp(models.Model):
    name=models.CharField(max_length=255)
    dob=models.DateField()
    file=models.FileField(upload_to="emp_file",null=True)
    doj=models.DateField(null=True)
    text_body=RichTextField(blank=True, null=True)