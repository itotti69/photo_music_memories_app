# Generated by Django 3.2.16 on 2022-11-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0017_alter_post_music_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='music',
            field=models.FileField(blank=True, upload_to='music/'),
        ),
    ]
