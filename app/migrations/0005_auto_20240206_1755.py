# Generated by Django 5.0.1 on 2024-02-06 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_paragraphword_id'),
    ]

    operations = [migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'),
    ]