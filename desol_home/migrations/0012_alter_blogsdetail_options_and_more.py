# Generated by Django 5.0.3 on 2024-04-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desol_home", "0011_blogsdetail"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogsdetail",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="blogsdetail",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]