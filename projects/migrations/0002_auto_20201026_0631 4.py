# Generated by Django 3.1.2 on 2020-10-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='startDate',
            field=models.DateField(),
        ),
    ]
