from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Caboutus(models.Model):
    para_num=models.IntegerField()
    aboutus_desc=HTMLField()