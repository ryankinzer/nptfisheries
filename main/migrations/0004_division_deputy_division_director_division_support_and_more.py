# Generated by Django 4.0.5 on 2022-06-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_division_division_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='deputy',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='director',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='division',
            name='support',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='projectleader',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
