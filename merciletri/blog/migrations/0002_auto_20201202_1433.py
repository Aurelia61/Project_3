# Generated by Django 3.1.4 on 2020-12-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pickup_line',
            field=models.CharField(default='', max_length=150, verbose_name="phrase d'accroche"),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=80, verbose_name='titre'),
        ),
    ]
