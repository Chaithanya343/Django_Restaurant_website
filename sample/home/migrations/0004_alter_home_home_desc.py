# Generated by Django 4.2.3 on 2024-12-27 05:36

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_home_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='home_desc',
            field=tinymce.models.HTMLField(),
        ),
    ]
