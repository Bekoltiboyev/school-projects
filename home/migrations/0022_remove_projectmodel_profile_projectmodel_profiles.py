# Generated by Django 4.2.3 on 2023-09-09 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='profile',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.profile'),
        ),
    ]
