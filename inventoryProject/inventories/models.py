import datetime
from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        db_table= 'categories'
        
class Inventories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    unitName = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField()
    unitCode = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=False, blank=False)
    purchasePrice= models.IntegerField()
    purchaseYear = models.IntegerField()
    
    class Meta:
        db_table= 'inventories'
        
class Staff(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    staffName = models.CharField(max_length=100, null=False, blank=False)
    staffPosition = models.CharField(max_length=100, null=False, blank=False)
    
    class Meta:
        db_table= 'staff'
    
class MaintenanceInventories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    inventory = models.ForeignKey(Inventories, on_delete=models.CASCADE)
    maintenanceDate = models.DateTimeField( blank=False)
    maintenanceVendor = models.CharField(max_length=100, null=False, blank=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    class Meta:
        db_table= 'maintenance_inventories'
    