# Generated by Django 3.1.1 on 2020-09-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Awesome Blog', max_length=255),
        ),
    ]
