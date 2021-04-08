# Generated by Django 3.2 on 2021-04-08 14:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_yt_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/aboutus/%Y/%m/%d/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
