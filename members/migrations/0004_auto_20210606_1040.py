# Generated by Django 2.2.10 on 2021-06-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210606_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='pic.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
