# Generated by Django 5.0.3 on 2024-03-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desol_home", "0007_customerreview"),
    ]

    operations = [
        migrations.CreateModel(
            name="FaqSection",
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
                ("question", models.CharField(blank=True, max_length=255, null=True)),
                ("answer", models.TextField(blank=True, default="", null=True)),
            ],
        ),
    ]