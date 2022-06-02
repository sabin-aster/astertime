from django.db import models
from nepali_datetime_field.models import NepaliDateField
# Create your models here.

status1 = [
    ('Regular','Regular')
 ]

status2 = [
    ('2078/79','2078/79'),
    ('2079/80','2079/80'),
]
status3 = [
    ('Public','Public Holiday'),
    ('International','International'),
    ('Active','Active Holiday'),
    ('Other','Other Holiday')
]
status4 = [
        ('A','Active'),
        ('I','Inactive'),
        ('T','Terminated'),
        ('B','Blacklisted')
    ]

class HRCalendar(models.Model):
    Work_Shift = models.CharField(max_length=50,choices=status1)
    HR_Year = models.CharField(max_length=8,choices=status2)
    nepali_date = NepaliDateField()
    Holiday_Title = models.CharField(max_length=50,choices=status3)
    Status = models.CharField(max_length=50,choices=status4)
    class Meta:
        verbose_name = 'HRCalendar'
        verbose_name_plural = 'HRCalendar'
    

    def __str__(self):
        return self.Holiday_Title








