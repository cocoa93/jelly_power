# Generated by Django 2.1a1 on 2018-06-06 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180606_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimg',
            name='img_news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News'),
        ),
    ]
