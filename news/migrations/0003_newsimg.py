# Generated by Django 2.1a1 on 2018-06-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180606_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImg',
            fields=[
                ('img_id', models.IntegerField(primary_key=True, serialize=False)),
                ('img_item', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
            ],
        ),
    ]
