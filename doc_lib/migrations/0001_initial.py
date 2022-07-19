# Generated by Django 4.0.5 on 2022-07-19 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('primary_author', models.CharField(max_length=30)),
                ('secondary_authors', models.CharField(max_length=255, null=True)),
                ('publish_date', models.DateField()),
                ('document_type', models.CharField(max_length=30, null=True)),
                ('keywords', models.CharField(max_length=60, null=True)),
                ('file', models.FileField(upload_to='documents/')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
