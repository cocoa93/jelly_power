# Generated by Django 2.1a1 on 2018-06-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]
