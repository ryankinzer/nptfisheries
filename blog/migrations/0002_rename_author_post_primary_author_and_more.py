# Generated by Django 4.0.5 on 2022-07-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='primary_author',
        ),
        migrations.AddField(
            model_name='post',
            name='secondary_authors',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
