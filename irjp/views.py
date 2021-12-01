from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration
from .forms import RegistrationForm

# Create your views here.


def home(request):
    return render(request, 'Home.html')
   
def Register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'Register.html', context)

def login2(request): 
    return render(request, 'T-login.html')

def table(request):
    registration_data = Registration.objects.all()
    
    getdata = {
        'data': registration_data
    }
    return render(request, 'table.html', getdata)

def edittable(request, data_id):
    student_data = Registration.objects.get(id=data_id)
    form = RegistrationForm(request.POST or None, instance=student_data)

    context = {
        "form": form,
        "student": student_data
        }
    
    if form.is_valid():
        form.save()
        return redirect('table')

    return render(request, 'edittable.html', context)


def delete_data(request, data_id):
    student_info = Registration.objects.get(id=data_id)

    if request.method == "POST":
        student_info.delete()
        return redirect('table')


    return render(request, 'delete_data.html', {'student_info': student_info})
    