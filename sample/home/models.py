from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class home(models.Model):
    para_num=models.IntegerField()
    home_desc=HTMLField()
    home_img = models.ImageField(upload_to='home_images/')  # Uploaded images will be stored in MEDIA_ROOT/home_images