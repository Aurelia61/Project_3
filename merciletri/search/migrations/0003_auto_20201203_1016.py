# Generated by Django 3.1.4 on 2020-12-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20201203_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='time',
        ),
        migrations.AddField(
            model_name='collectlocation',
            name='time',
            field=models.ManyToManyField(to='search.Time'),
        ),
    ]
