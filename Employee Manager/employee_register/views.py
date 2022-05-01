from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = EmployeeForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Empregado correspondentes à chave primária referente ao id
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance = employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir um novo empregado
            form = EmployeeForm(request.POST)
        else: # Operação de atualizar um empregado já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid(): 
            form.save()
        return redirect('/employee/list')            

def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employee/list')

