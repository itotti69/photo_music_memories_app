# Generated by Django 3.2.16 on 2022-11-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0032_post_spot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]