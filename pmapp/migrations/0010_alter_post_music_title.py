# Generated by Django 3.2.16 on 2022-11-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0009_post_music_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='music_title',
            field=models.CharField(default='', max_length=50, verbose_name='曲名'),
        ),
    ]