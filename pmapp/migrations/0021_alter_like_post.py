# Generated by Django 3.2.16 on 2022-11-27 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0020_post_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmapp.post', verbose_name='投稿'),
        ),
    ]
