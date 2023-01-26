# Generated by Django 4.1.5 on 2023-01-26 11:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('unitName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unitCode', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('purchasePrice', models.IntegerField()),
                ('purchaseYear', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.category')),
            ],
            options={
                'db_table': 'inventories',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('staffName', models.CharField(max_length=100)),
                ('staffPosition', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceInventories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('maintenanceDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('maintenanceVendor', models.CharField(max_length=100)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.inventories')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.staff')),
            ],
            options={
                'db_table': 'maintenance_inventories',
            },
        ),
    ]
