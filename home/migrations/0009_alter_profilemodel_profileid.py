# Generated by Django 4.2.1 on 2023-09-05 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_profilemodel_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profileID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
