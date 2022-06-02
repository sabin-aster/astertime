
from django import forms
from .models import Employee
from crispy_forms.layout import Layout, Div, Field, Row, Submit, Button, Column

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder
from crispy_forms.layout import Field
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
status1 = (
        ('A','Active'),
        ('I','Inactive'),
        ('T','Terminated'),
        ('B','Blacklisted')
)

status2 = (
        ('1','Mr.'),
        ('2','Miss'),
        ('3','Mrs')
)


status3 = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
 )

 
status4 = (
        ('A','A'),
        ('B','B'),
        ('C','C')
)

status8 = [
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
        ('Quarterly','Quarterly'),
        ('Annualy','Annualy')
    ]

status5 = (
    ('5000','')
)

status9=[('50000','5000'),
  ('3.00%','3.00%')]


status7  = (
        ('Y','Yes'),
        ('N','No'),
        ('Decided','TBD')
)


status10 = [

        ('A+','A+'),
        ('O+','O+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('O-','O-'),
        ('B-','B-'),
        ('AB-','AB-')
    ]
class EmployeeModelForm(forms.ModelForm):
    Employee_Status = forms.ChoiceField(choices = status1)
    Employee_Id = forms.IntegerField()
    Employee_Number = forms.IntegerField()
    PAN_Number = forms.IntegerField(required=False)
    Employee_Name_Initials = forms.CharField()
    Last_Name = forms.CharField()
    First_Name = forms.CharField()
    Middle_Name = forms.CharField(required=False)
    Full_Name = forms.CharField()

    Title = forms.ChoiceField(choices=status2)
    Date_Of_Birth = forms.DateField()
    Date_Of_Joined = forms.DateField()

    Probation_Period = forms.IntegerField(required=False)
    Date_Of_Confirmation = forms.DateField(required=False)
    Date_Of_Resignation = forms.DateField(required=False)

    Last_Date_Work  = forms.DateField(required=False)
    Designation = forms.CharField()
    Salary_Tier = forms.ChoiceField(choices=status3,required=False)


    Grade = forms.ChoiceField(choices=status4,required=False)
    Daily_Attendance_Enable = forms.ChoiceField(choices=status7,required=False)
    TDS_Enable = forms.ChoiceField(choices=status7,required=False)


    
    PF_Enable = forms.ChoiceField(choices=status7,required=False)
    TF_Enable = forms.ChoiceField(choices=status7,required=False)
    Staff_Welfare = forms.ChoiceField(choices=status9,required=False,widget=forms.RadioSelect)

    
    Sports_Fund = forms.CharField(required=False)
    CSR_Foundation_Fund = forms.CharField(required=False)
    Staff_Loan_Entitlement = forms.ChoiceField(choices=status7,required=False)


    Limit_Loan = forms.IntegerField(required=False)
    Term_Repayment = forms.ChoiceField(choices=status8,required=False)
    LOO_Issued_Date = forms.DateField(required=False)


    LOA_Issued_Date = forms.DateField(required=False)
    NDA_Signed_Date = forms.DateField(required=False)
    Resignation_Recorded_Date = forms.DateField(required=False)

    
    Resignation_Approved_Date = forms.DateField(required=False)
    Service_Letter_Issued_Date =  forms.DateField(required=False)
    Bank_Name_and_Code = forms.CharField(required=False)

    Bank_Branch_Name_and_Code = forms.CharField(max_length=500,required=False)
    Bank_Account = forms.IntegerField(required=False)
    Bank_Account_Number = forms.IntegerField(required=False)


    Medical_History = forms.CharField(max_length=300,required=False)
    Employee_Mobile_Number = forms.IntegerField(required=False)
    Emergency_Relative_Mobile_Number = forms.IntegerField(required=False)


    Emergency_Relative_Name = forms.CharField(max_length=200,required=False)
    Emergency_Relative_Relations = forms.CharField(max_length=200,required=False)
    Emergency_Blood_Group =  forms.ChoiceField(choices=status10,required=False)



    class Meta:
        model = Employee
        fields= "__all__"
        
        