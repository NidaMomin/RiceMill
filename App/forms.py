from django import forms
from .models import Employee, Transaction, RawMaterial, Machine, SalesTable

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'mobile', 'salary', 'emp_id', 'position']
        widgets = {
            'salary': forms.TextInput(attrs={'class': 'form-control'}),  # Use TextInput to remove spinners
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'account_holder']
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'transaction_type': 'Type of Transaction',
            'amount': 'Transaction Amount',
            'account_holder': 'Account Holder Name',
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError('Amount must be greater than zero.')
        return amount

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = ['material_name', 'supplier_name', 'unit_of_measure', 'cost_per_unit']
        widgets = {
            'cost_per_unit': forms.TextInput(attrs={'class': 'form-control'}),  # Use TextInput to remove spinners
        }

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name', 'maintenance_date', 'operational_status', 'spare_parts_stock', 'repair_cost']
        widgets = {
            'maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Date picker
        }

class SalesTableForm(forms.ModelForm):
    class Meta:
        model = SalesTable
        fields = ['name', 'phone_number', 'address', 'payment_terms', 'date', 'total_amount', 'payment_status', 'remarks']
        widgets={
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),  # Control height with rows
        }

