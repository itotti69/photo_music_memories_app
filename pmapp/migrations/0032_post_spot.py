# Generated by Django 3.2.16 on 2022-11-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0031_auto_20221127_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='spot',
            field=models.CharField(blank=True, max_length=50, verbose_name='写真スポット'),
        ),
    ]
