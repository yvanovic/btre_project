# Generated by Django 4.1.4 on 2023-04-24 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("listing", models.CharField(max_length=200)),
                ("listing_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("message", models.TextField(blank=True)),
                ("contact_date", models.DateTimeField(default=datetime.datetime.now)),
                ("user_id", models.IntegerField(blank=True)),
            ],
        ),
    ]
