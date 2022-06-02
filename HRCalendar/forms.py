from nepali_datetime_field.forms import NepaliDateField
from django import forms
from .models import HRCalendar

    



 
# create a ModelForm
class HRCalendarModelForm(forms.ModelForm):
    nepali_date = NepaliDateField()

    # specify the name of model to use
    class Meta:
        model = HRCalendar
        fields = "__all__"
        