# Generated by Django 5.0.7 on 2024-09-11 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_payment_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='attendee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.attendee'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('attendee', 'invoice')},
        ),
    ]
