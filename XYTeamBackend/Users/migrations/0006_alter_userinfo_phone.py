# Generated by Django 4.2 on 2024-08-03 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0005_userinfo_credit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="phone",
            field=models.PositiveBigIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(10000000000),
                    django.core.validators.MaxValueValidator(99999999999),
                ],
            ),
        ),
    ]
