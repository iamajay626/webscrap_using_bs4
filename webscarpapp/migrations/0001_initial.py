# Generated by Django 5.0.1 on 2024-02-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('string_name', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
