# Generated by Django 4.0.5 on 2022-06-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_division_deputy_division_director_division_support_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='deputy',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='support',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]