# Generated by Django 5.2.4 on 2025-07-27 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('reservation_date', 'reservation_slot')},
        ),
    ]
