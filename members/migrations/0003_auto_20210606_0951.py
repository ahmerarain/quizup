# Generated by Django 2.2.10 on 2021-06-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210606_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
