# Generated by Django 3.1.4 on 2020-12-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_school_std'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='std',
            field=models.IntegerField(blank=True, choices=[('1', 1), ('2', 2)], null=True),
        ),
    ]