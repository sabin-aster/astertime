from django.contrib import admin
from django.urls import path,include
from .import views
from django.shortcuts import render


# def administrator(request):
#     return render(request,'Employee/admin_index.html')

app_name = 'employee'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.login,name='login'),
    
    path('employee/',views.employee,name='employee'),
    
]