# Generated by Django 5.0.7 on 2024-09-12 03:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0012_catering_user_event_user_eventlogistics_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="attendee",
            old_name="client",
            new_name="user",
        ),
    ]
