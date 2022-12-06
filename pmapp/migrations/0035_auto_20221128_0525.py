# Generated by Django 3.2.16 on 2022-11-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0034_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1, verbose_name='本文'),
            preserve_default=False,
        ),
    ]
