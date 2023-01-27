from django.urls import path

from inventories import views


urlpatterns = [
    path('category', views.category.CategoryList.as_view()),
    path('category/<id>', views.category.CategoryDetail.as_view()),
    path('staff', views.staff.StaffList.as_view()),
    path('staff/<id>', views.staff.StaffDetail.as_view()),
    
    path('inventories', views.inventories.InventoriesList.as_view()),
    path('inventory/<id>', views.inventories.InventoryDetail.as_view()),
  
    path('maintenanceInventories', views.maintenanceInventories.MaintenanceInventoriesList.as_view()),
    path('maintenanceInventory/<id>', views.maintenanceInventories.MaintenanceInventoryDetail.as_view()),
  

]