from django.contrib import admin
from .models import Employee
from .models import Transaction

admin.site.register(Employee) 
admin.site.register(Transaction)