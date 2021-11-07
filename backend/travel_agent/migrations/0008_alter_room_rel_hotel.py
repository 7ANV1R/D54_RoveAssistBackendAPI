# Generated by Django 3.2.8 on 2021-11-06 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agent', '0007_rename_hotel_room_rel_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rel_hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='root_hotels', to='travel_agent.hotel'),
        ),
    ]