from django.db import models
from ckeditor.fields import RichTextField
import datetime
# Create your models here.
class Djform(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField()
    website=models.URLField()
    text_area=RichTextField()
    word_count=models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"), blank=True)