# Generated by Django 4.2.1 on 2023-09-29 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_alter_projectmodel_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]