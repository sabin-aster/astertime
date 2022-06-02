from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeModelForm
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login

# def home(request):
#     return render(request,'')


def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'Employee/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page?
            return HttpResponseRedirect('/employee/')
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            
            return render(request, 'Employee/login.html', {'context': context})


def employee(request):
    if request.method == 'POST':
        print('okkkkkkkkkkkkkkkkkkk')
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            print('Yes....')
            # process form data
            #gets new object
            form.save()
            return HttpResponseRedirect('/')
    context ={}
    context['form']= EmployeeModelForm()
    return render(request, "Employee/employee.html",context)
