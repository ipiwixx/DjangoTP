# Generated by Django 5.0 on 2023-12-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='note',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
