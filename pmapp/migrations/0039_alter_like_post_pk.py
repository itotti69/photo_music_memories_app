# Generated by Django 3.2.16 on 2022-11-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0038_like_post_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post_pk',
            field=models.IntegerField(blank=True, verbose_name='投稿ID'),
        ),
    ]