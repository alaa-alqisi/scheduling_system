# Generated by Django 3.2.11 on 2022-01-15 23:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 23, 45, 35, 485732, tzinfo=utc)),
        ),
    ]
