# Generated by Django 4.0.3 on 2022-12-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0008_alter_appointment_service_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(max_length=50),
        ),
    ]
