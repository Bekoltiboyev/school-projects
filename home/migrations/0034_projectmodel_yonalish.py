# Generated by Django 4.2.3 on 2023-09-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_remove_profile_project_projectmodel_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='yonalish',
            field=models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend')], default='Frontend', max_length=20),
        ),
    ]
