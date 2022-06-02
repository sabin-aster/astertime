from django.shortcuts import render
from .forms import HRCalendarModelForm
# Create your views here.


def hr(request):
    context ={}
    context['form']= HRCalendarModelForm()
    return render(request, "HRCalendar/hrcalendar.html", context)