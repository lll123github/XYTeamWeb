# Generated by Django 4.2 on 2024-05-31 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                ("phone", models.PositiveBigIntegerField(blank=True, null=True)),
                (
                    "TMPID",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("TMPName", models.CharField(blank=True, max_length=20, null=True)),
                ("steamID", models.PositiveBigIntegerField(blank=True, null=True)),
                ("QQ", models.PositiveBigIntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
