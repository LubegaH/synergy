# Generated by Django 2.1 on 2018-10-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.CharField(max_length=280, null=True),
        ),
    ]