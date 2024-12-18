# Generated by Django 4.1.2 on 2024-12-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CodeSubmission",
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
                ("title", models.CharField(max_length=255)),
                ("language", models.CharField(max_length=50)),
                ("code", models.TextField()),
                ("review_result", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
