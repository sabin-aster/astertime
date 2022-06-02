from django.db import models


# Create your models here.






class Employee(models.Model):
    status1 = [
        ('A','Active'),
        ('I','Inactive'),
        ('T','Terminated'),
        ('B','Blacklisted')
    ]

    status2 = [
        ('1','Mr.'),
        ('2','Miss'),
        ('3','Mrs')
    ]

    status3 = [
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
    ]

    status4 = [
        ('A','A'),
        ('B','B'),
        ('C','C')
    ]
   
    status5 = [
        ('Local','Local Consultant'),
        ('International','International Consultant'),
        ('Permanent','Permanent'),
        ('Casual','Casual'),
        ('WFH','WFH'),
        ('WFO','WFO')
    ]


    status6 = [
    ('Regular','Regular')

]
    status7  =[
        ('Y','Yes'),
        ('N','No'),
        ('Decided','TBD')
    ]

    status8 = [
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
        ('Quarterly','Quarterly'),
        ('Annualy','Annualy')
    ]

    status9 = [

        ('A+','A+'),
        ('O+','O+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('O-','O-'),
        ('B-','B-'),
        ('AB-','AB-')
    ]

    Employee_Status = models.CharField(max_length=2,choices=status1,default='Active')
    Employee_Id = models.IntegerField()
    Employee_Number = models.IntegerField()
    PAN_Number = models.BigIntegerField(blank=True,null=True)
    Employee_Name_Initials = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100,blank=True,null=True)
    Full_Name = models.CharField(max_length=100)
    
    Title = models.CharField(max_length=2,choices=status2)
    Date_Of_Birth = models.DateField()
    Date_of_Joined = models.DateField()

    Probation_Period = models.IntegerField(blank=True,null=True)
    Date_Of_Confirmation = models.DateField(blank=True,null=True)
    Date_Of_Resignation = models.DateField(blank=True,null=True)
    
    Last_Date_Work = models.DateField(blank=True,null=True)
    Designation = models.CharField(max_length=100)
    Salary_Tier = models.CharField(max_length=2,choices=status3,blank=True,null=True)


    Grade = models.CharField(max_length=2,choices=status4,blank=True,null=True)
    Daily_Attendance_Enable = models.CharField(max_length=7,choices=status7,blank=True,null=True)
    TDS_Enable = models.CharField(max_length=7,choices=status7,blank=True,null=True)

    PF_Enable = models.CharField(max_length=7,choices=status7,blank=True,null=True)
    TF_Enable = models.CharField(max_length=7,choices=status7,blank=True,null=True)
    Staff_Welfare = models.CharField(max_length=7,blank=True,null=True)

    Sports_Fund = models.CharField(max_length = 7,blank=True,null=True)
    CSR_Foundation_Fund = models.CharField(max_length=7,blank=True,null=True)
    Staff_Loan_Entitlement = models.CharField(max_length=7,choices=status7,blank=True,null=True)

    Limit_Loan = models.IntegerField()
    Term_Repayment = models.CharField(max_length=30,choices=status8)
    LOO_Issued_Date = models.DateField(blank=True,null=True)

    LOA_Issued_Date = models.DateField(blank=True,null=True)
    NDA_Signed_Date = models.DateField(blank=True,null=True)
    Resignation_Recorded_Date = models.DateField(blank=True,null=True)

    Resignation_Approved_Date = models.DateField(blank=True,null=True)
    Service_Letter_Issued_Date =  models.DateField(blank=True,null=True)
    Bank_Name_and_Code = models.CharField(max_length=500,blank=True,null=True)

    Bank_Branch_Name_and_Code = models.CharField(max_length=500,blank=True,null=True)
    Bank_Account = models.BigIntegerField(blank=True,null=True)
    Bank_Account_Number = models.BigIntegerField(blank=True,null=True)


    Medical_History = models.CharField(max_length=300,blank=True,null=True)
    Employee_Mobile_Number = models.BigIntegerField(blank=True,null=True)
    Emergency_Relative_Mobile_Number = models.BigIntegerField(blank=True,null=True)

    Emergency_Relative_Name = models.CharField(max_length=200,blank=True,null=True)
    Emergency_Relative_Relations = models.CharField(max_length=200,blank=True,null=True)
    Emergency_Blood_Group =  models.CharField(max_length= 4,choices=status9,blank=True,null=True)
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'
    


    def __str__(self):
        return self.Full_Name



    # Sports_Fund
    

