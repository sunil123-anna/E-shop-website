# Generated by Django 3.1.5 on 2021-02-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
