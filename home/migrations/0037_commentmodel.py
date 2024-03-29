# Generated by Django 4.2.3 on 2023-09-30 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_projectmodel_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.projectmodel')),
            ],
        ),
    ]
