# Generated by Django 5.0.7 on 2024-09-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0014_vendor_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="ticket_quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
