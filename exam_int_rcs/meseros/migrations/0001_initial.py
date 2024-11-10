# Generated by Django 5.1.3 on 2024-11-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meseros",
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
                ("nombre", models.CharField(max_length=40)),
                ("nacionalidad", models.CharField(default="", max_length=30)),
                ("edad", models.IntegerField(default=0)),
            ],
        ),
    ]
