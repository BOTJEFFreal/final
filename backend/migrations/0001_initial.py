# Generated by Django 4.2.3 on 2023-07-16 09:39

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "input_file1",
                    models.FileField(upload_to=backend.models.input_file_path),
                ),
                ("text_input1", models.CharField(max_length=100)),
                ("text_input2", models.CharField(max_length=100)),
                ("text_input3", models.CharField(max_length=100)),
                ("text_input4", models.CharField(max_length=100)),
                (
                    "output_file",
                    models.FileField(upload_to=backend.models.output_file_path),
                ),
            ],
        ),
    ]
