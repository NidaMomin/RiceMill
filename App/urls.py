from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('employee/', views.employee_form, name='employee_insert'),  # GET and POST request for insert operation
    path('employee/<int:id>/', views.employee_form, name='employee_update'),  # GET and POST request for update operation
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),  # URL for deleting an employee
    path('employee/list/', views.employee_list, name='employee_list'),  # GET request to retrieve and display all records

    path('transaction/', views.create_transaction, name='transaction_create'),  # URL for creating a transaction
    path('transaction/<int:id>/', views.transaction_update, name='transaction_update'),  # URL for updating a transaction
    path('transaction/delete/<int:id>/', views.transaction_delete, name='transaction_delete'),  # URL for deleting a transaction
    path('transaction/list/', views.transaction_list, name='transaction_list'),  # URL for listing transactions
    
    path('raw-material/', views.raw_material_form, name='raw_material_insert'),  # GET and POST request for insert operation
    path('raw-material/<int:id>/', views.raw_material_form, name='raw_material_update'),  # GET and POST request for update operation
    path('raw-material/delete/<int:id>/', views.raw_material_delete, name='raw_material_delete'),  # URL for deleting a raw material
    path('raw-material/list/', views.raw_material_list, name='raw_material_list'),  # GET request to retrieve and display all raw materials

    path('mac/', views.machine_create, name='machine_create'),  # Create a new machine
    path('mac/update/<int:id>/', views.machine_update, name='machine_update'),  # Update a machine
    path('mac/delete/<int:pk>/', views.machine_delete, name='machine_delete'),  # Delete a machine
    path('mac/list/', views.machine_list, name='machine_list'),  # List of machines

    path('sales/', views.sales_form, name='sales_create'),
    path('sales/update/<int:id>/', views.sales_update, name='sales_update'),
    path('sales/delete/<int:id>/', views.sales_delete, name='sales_delete'),
    path('sales/list', views.sales_list, name='sales_list'),
]
