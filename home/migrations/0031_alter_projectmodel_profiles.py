# Generated by Django 4.2.3 on 2023-09-21 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_projectmodel_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='profiles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.profile'),
        ),
    ]
