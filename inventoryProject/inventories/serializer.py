from rest_framework import serializers

from inventories.models import Category, Inventories, Staff, MaintenanceInventories
     
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class InventoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventories
        fields = (
            'id',
            'unitName',
            'quantity',
            'unitCode',
            'type',
            'purchasePrice',
            'purchaseYear',
            'category'
        )

      # 
class MaintenanceInventoriesDetailSerializer(serializers.ModelSerializer):
    inventory = InventoriesSerializer()
    class Meta:
        model = MaintenanceInventories
        # fields = ['inventory']
        fields = (
            'inventory',
            'maintenanceDate'
        )

# 
class StaffDetailSerializer(serializers.ModelSerializer):
    maintenanceInventories = MaintenanceInventoriesDetailSerializer(many=True, source='maintenance_staff')
    
    class Meta:
        model = Staff
        fields = (
            'id',
            'staffName',
            'staffPosition',
            'maintenanceInventories'
        )
#   

class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = (
            'id',
            'staffName',
            'staffPosition'
        )
  

    
class InventoriesShowSerializer(serializers.ModelSerializer):
     
    category = CategorySerializer()
    
    class Meta:
        model = Inventories
        fields = (
            'id',
            'unitName',
            'quantity',
            'unitCode',
            'type',
            'purchasePrice',
            'purchaseYear',
            'category'
        )
    
class MaintenanceInventoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MaintenanceInventories
        fields = (
            'id',
            'maintenanceDate',
            'maintenanceVendor',
            'inventory',
            'staff'
        )
    
class MaintenanceInventoriesShowSerializer(serializers.ModelSerializer):
     
    inventory = InventoriesShowSerializer()
    staff = StaffSerializer()

    class Meta:
        model = MaintenanceInventories
        fields = (
           'id',
            'maintenanceDate',
            'maintenanceVendor',
            'inventory',
            'staff'
        )

