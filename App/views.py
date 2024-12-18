from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, TransactionForm, RawMaterialForm, MachineForm, SalesTableForm
from .models import Employee, Transaction, Material, RawMaterial, Machine, SalesTable
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'App/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def home(request):
    employees = Employee.objects.all()
    raw_materials = RawMaterial.objects.all()
    sales = SalesTable.objects.all()
    machines = Machine.objects.all()
    transactions = Transaction.objects.all()
    
    context = {
        'employees': employees,
        'raw_materials': raw_materials,
        'sales': sales,
        'machines': machines,
        'transactions': transactions,
    }
    return render(request, 'App/home.html', context)

# Employee Views
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "App/employee_list.html", context)

def employee_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        if id == 0:
            form = EmployeeForm()
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(instance=employee)

    return render(request, "App/employee_form.html", {'form': form})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('employee_list')

# Transaction Views


def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new transaction to the database
            return redirect('transaction_list')  # Redirect to the transaction list view
    else:
        form = TransactionForm()  # Create a new empty form

    return render(request, 'App/create_transaction.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()  # Fetch all transactions from the database
    return render(request, 'App/transaction_list.html', {'transaction_list': transactions})

def transaction_update(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()  # Update the transaction
            return redirect('transaction_list')  # Redirect to the transaction list view
    else:
        form = TransactionForm(instance=transaction)  # Pre-fill the form with the existing transaction data

    return render(request, 'App/create_transaction.html', {'form': form})

def transaction_delete(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    transaction.delete()  # Delete the transaction
    return redirect('transaction_list')  # Redirect to the transaction list view

# Raw Material Views
def create_raw_material(request):
    if request.method == 'POST':
        # Assuming you have a form that submits the necessary data
        material = Material.objects.create(type=request.POST['material_type'])
        material = RawMaterial.objects.create(
            supplier_name=request.POST['supplier_name'],
            unit_of_measure=request.POST['unit_of_measure'],
            cost_per_unit=request.POST['cost_per_unit'],
            material_name=material
        )
        return redirect('raw_material_list')  # Redirect to a success page or another view

    return render(request, 'App/raw_material_form.html')  # Render a form template


def raw_material_list(request):
    raw_materials = RawMaterial.objects.all()
    for material in raw_materials:
        print(f"Raw Material ID: {material.material_id}")
    return render(request, 'App/raw_material_list.html', {'raw_materials': raw_materials})

def raw_material_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = RawMaterialForm(request.POST)
        else:
            raw_material = get_object_or_404(RawMaterial, pk=id)
            form = RawMaterialForm(request.POST, instance=raw_material)

        if form.is_valid():
            form.save()
            return redirect('raw_material_list')
    else:
        if id == 0:
            form = RawMaterialForm()
        else:
            raw_material = get_object_or_404(RawMaterial, pk=id)
            form = RawMaterialForm(instance=raw_material)

    return render(request, "App/raw_material_form.html", {'form': form})

def raw_material_delete(request, id):
    raw_material = get_object_or_404(RawMaterial, pk=id)
    raw_material.delete()
    return redirect('raw_material_list')


# List all machines
def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'App/machine_list.html', {'machines': machines})

# Create a new machine
def machine_create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine_list')  # Redirect to the machine list after saving
    else:
        form = MachineForm()  # Create a new form instance for GET requests
    return render(request, 'App/machine_form.html', {'form': form})

# Update an existing machine
def machine_update(request, id):
    machine = get_object_or_404(Machine, pk=id)  # Fetch the machine or return 404
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)  # Bind the form to the instance
        if form.is_valid():
            form.save()
            return redirect('machine_list')  # Redirect to the machine list after saving
    else:
        form = MachineForm(instance=machine)  # Create a form instance with the existing machine data
    return render(request, 'App/machine_form.html', {'form': form})

# Delete a machine
def machine_delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)  # Fetch the machine or return 404
    if request.method == 'POST':
        machine.delete()  # Delete the machine
        return redirect('machine_list')  # Redirect to the machine list after deletion
    return render(request, 'App/machine_confirm_delete.html', {'machine': machine})

#Sales details
def sales_list(request):
    sales_entries = SalesTable.objects.all()
    return render(request, 'App/sales_list.html', {'sales_entries': sales_entries})

def sales_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = SalesTableForm(request.POST)
        else:
            sales_entry = get_object_or_404(SalesTable, pk=id)
            form = SalesTableForm(request.POST, instance=sales_entry)

        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        if id == 0:
            form = SalesTableForm()
        else:
            sales_entry = get_object_or_404(SalesTable, pk=id)
            form = SalesTableForm(instance=sales_entry)

    return render(request, "App/sales_form.html", {'form': form})

def sales_update(request, id):
    salesTable = get_object_or_404(SalesTable, pk=id)
    if request.method == 'POST':
        form = SalesTableForm(request.POST, instance=salesTable)
        if form.is_valid():
            form.save()  # Update the sales
            return redirect('sales_list')  # Redirect to the sales list view
    else:
        form = SalesTableForm(instance=salesTable)  # Pre-fill the form with the existing sales data

    return render(request, 'App/sales_form.html', {'form': form})

def sales_delete(request, id):
    sales_entry = get_object_or_404(SalesTable, pk=id)
    sales_entry.delete()
    return redirect('sales_list')
