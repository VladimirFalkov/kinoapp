# Generated by Django 5.0 on 2023-12-17 18:50

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="poster",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, null=True, upload_to="movie/posters"
            ),
        ),
    ]