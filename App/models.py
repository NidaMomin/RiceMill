from django.db import models
from django.core.exceptions import ValidationError


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateField(auto_now_add=True)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_holder = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount} on {self.transaction_date}"

    class Meta:
        ordering = ['-transaction_date']  # Example of ordering by date
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
   
class Material(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    
class RawMaterial(models.Model):
    material_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=20)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    material_name = models.ForeignKey(Material, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.material_name
    

class Machine(models.Model):
    MACHINE_STATUS_CHOICES = [
        ('Running', 'Running'),
        ('Idle', 'Idle'),
        ('Faulty', 'Faulty'),
    ]

    machine_name = models.CharField(max_length=100)
    maintenance_date = models.DateField()
    operational_status = models.CharField(max_length=10,choices=MACHINE_STATUS_CHOICES)
    spare_parts_stock = models.PositiveIntegerField()
    repair_cost = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.machine_name

class SalesTable(models.Model):
    REMARKS_STATUS_CHOICES = [
        ('Sale', 'Sale'),
        ('Purchase', 'Purchase'),
    ]
    PAYMENT_TYPE_CHOICES = [
        ('Netbanking', 'NetBanking'),
        ('Cash', 'Cash'),
        ('check', 'Check'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    id = models.AutoField(primary_key=True)  # Auto-generated primary key
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    payment_terms = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    remarks = models.CharField(max_length=10, choices=REMARKS_STATUS_CHOICES)

    class Meta:
        verbose_name = "Sales Table"
        verbose_name_plural = "Sales Tables"

    def __str__(self):
        return f"{self.name} - {self.date}"