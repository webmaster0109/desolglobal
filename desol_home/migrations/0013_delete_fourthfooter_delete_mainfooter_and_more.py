# Generated by Django 5.0.3 on 2024-04-08 12:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("desol_home", "0012_alter_blogsdetail_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="FourthFooter",
        ),
        migrations.DeleteModel(
            name="MainFooter",
        ),
        migrations.RemoveField(
            model_name="subheaderitems",
            name="main_header",
        ),
        migrations.DeleteModel(
            name="SecondFooter",
        ),
        migrations.DeleteModel(
            name="ShortAboutDescription",
        ),
        migrations.DeleteModel(
            name="ThirdFooter",
        ),
        migrations.AlterModelOptions(
            name="blogsdetail",
            options={"ordering": ["-created_at"]},
        ),
        migrations.DeleteModel(
            name="MainHeaderItems",
        ),
        migrations.DeleteModel(
            name="SubHeaderItems",
        ),
    ]
