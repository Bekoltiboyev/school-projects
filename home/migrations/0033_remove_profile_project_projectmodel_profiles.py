# Generated by Django 4.2.3 on 2023-09-23 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_remove_projectmodel_profiles_profile_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='profiles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.profile'),
        ),
    ]
