# Generated by Django 5.0.3 on 2024-04-16 15:43

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boundary",
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
                ("name", models.CharField(max_length=100)),
                (
                    "boundary",
                    django.contrib.gis.db.models.fields.PolygonField(srid=4326),
                ),
                (
                    "parent_boundary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="upper_boundaries",
                        to="svsaweb.boundary",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MapLocation",
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
                ("name", models.CharField(max_length=100)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("zoom", models.IntegerField()),
                ("description", models.TextField()),
                (
                    "boundary",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="svsaweb.boundary",
                    ),
                ),
            ],
        ),
    ]
