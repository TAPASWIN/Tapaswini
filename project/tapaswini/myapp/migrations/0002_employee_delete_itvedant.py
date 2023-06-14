# Generated by Django 4.2.1 on 2023-06-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=90)),
                ("designation", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("join_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Itvedant",
        ),
    ]
