# Generated by Django 3.2.16 on 2022-11-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0007_post_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='music',
            field=models.FileField(upload_to='music/'),
        ),
    ]
