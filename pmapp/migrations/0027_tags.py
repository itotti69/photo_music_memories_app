# Generated by Django 3.2.16 on 2022-11-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0026_alter_post_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag名')),
                ('name_en', models.CharField(max_length=10, verbose_name='Tag名英語')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
