# Generated by Django 2.2 on 2020-03-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200327_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
