# Generated by Django 3.1.4 on 2020-12-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='std',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
