# Generated by Django 2.2.10 on 2021-06-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(),
        ),
    ]
