# Generated by Django 5.0.1 on 2024-02-06 12:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20240206_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraphword',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]