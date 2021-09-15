from django.shortcuts import render
from crudProject.models import crudEmployee
from django.contrib import messages
from crudProject.forms import employeeform


def employeeInsert(request):
    if request.method == "POST":
        if request.POST.get('ename') and request.POST.get('eaddress') and request.POST.get('age') and request.POST.get('egender'):
            save_employee = crudEmployee()
            save_employee.ename = request.POST.get("ename")
            save_employee.eaddress = request.POST.get("eaddress")
            save_employee.age = request.POST.get("age")
            save_employee.egender = request.POST.get("egender")
            save_employee.save()
            messages.success(request, "The record " +save_employee.ename+" Is Saved Successfully")
            return render(request, "create.html")
    else:
        return render(request, "create.html")


def employeeEdit(request, id):
    get_student_details = crudEmployee.objects.get(id=id)
    return render(request, "edit.html", {"crudEmployee": get_student_details})


def employeeDisplay(request):
    results = crudEmployee.objects.all()
    return render(request, "index.html", {"crudEmployee": results})


def employeeUpdate(request, id):
    employee_update = crudEmployee.objects.get(id=id)
    form = employeeform(request.POST, instance=employee_update)
    if form.is_valid():
        form.save()
        messages.success(request, "The Employee record got updated successfully")
        return render(request, "edit.html", {"crudEmployee": employee_update})


def employeeDelete(request, id):
    delete_student = crudEmployee.objects.get(id=id)
    delete_student.delete()
    results = crudEmployee.objects.all()
    return render(request, "index.html", {"crudEmployee": results})
