# Generated by Django 5.0.3 on 2024-03-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desol_home", "0008_faqsection"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoogleMapEmbed",
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
                ("embed_code", models.TextField(blank=True, default="", null=True)),
            ],
        ),
    ]