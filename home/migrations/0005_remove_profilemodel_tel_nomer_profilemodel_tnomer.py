# Generated by Django 4.2.3 on 2023-08-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_profilemodel_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='tel_nomer',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='tNomer',
            field=models.CharField(default=998, max_length=50),
        ),
    ]
