# Generated by Django 3.2.16 on 2022-11-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0018_alter_post_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=30, verbose_name='YouTubeのURL'),
        ),
    ]