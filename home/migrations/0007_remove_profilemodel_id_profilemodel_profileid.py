# Generated by Django 4.2.1 on 2023-09-05 15:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_profilemodel_user_alter_profilemodel_kurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='id',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='profileID',
            field=models.UUIDField(default=uuid.UUID('e6bb7532-5993-4eec-88b4-f10c7c9ab461'), primary_key=True, serialize=False),
        ),
    ]
