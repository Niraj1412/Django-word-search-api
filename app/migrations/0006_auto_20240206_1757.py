# Generated by Django 5.0.1 on 2024-02-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20240206_1755'),
    ]

    operations = [
    migrations.RunSQL('ALTER TABLE app_paragraphword DROP COLUMN id;'),
    migrations.RunSQL('ALTER TABLE app_paragraphword ADD COLUMN id UUID PRIMARY KEY DEFAULT uuid_generate_v4();'),
]

