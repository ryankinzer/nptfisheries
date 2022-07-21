# Generated by Django 4.0.5 on 2022-07-20 14:53

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, default='000-000-0000', help_text='Contact phone number', max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='title',
            field=models.CharField(default='Fish Expert', max_length=30),
        ),
    ]