# Generated by Django 4.1.5 on 2023-01-27 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0003_alter_maintenanceinventories_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceinventories',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_inventory', to='inventories.inventories'),
        ),
        migrations.AlterField(
            model_name='maintenanceinventories',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_staff', to='inventories.staff'),
        ),
    ]
