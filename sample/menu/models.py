from django.db import models

class menu(models.Model):
    menu_icom=models.CharField(max_length=10)
    menu_title=models.CharField(max_length=10)
    menu_des=models.TextField(max_length=100)
