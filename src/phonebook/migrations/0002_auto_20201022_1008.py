# Generated by Django 3.1.2 on 2020-10-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='phones',
        ),
        migrations.AddField(
            model_name='phone',
            name='phone',
            field=models.CharField(default='111', max_length=12, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]
