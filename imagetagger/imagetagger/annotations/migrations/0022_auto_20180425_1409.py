# Generated by Django 2.0 on 2018-04-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0021_exportformat_vector_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportformat',
            name='vector_format',
            field=models.CharField(default='x%%count1: %%x%%bry%%count1: %%y%%br', max_length=200),
        ),
    ]
