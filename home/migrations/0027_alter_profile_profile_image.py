# Generated by Django 4.2.3 on 2023-09-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]