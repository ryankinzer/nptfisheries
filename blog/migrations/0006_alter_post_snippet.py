# Generated by Django 4.0.5 on 2022-07-14 02:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=ckeditor.fields.RichTextField(default='Click link above to read blog post...', max_length=255),
        ),
    ]
