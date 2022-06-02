# Generated by Django 4.0.4 on 2022-05-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('T', 'Terminated'), ('B', 'Blacklisted')], default='Active', max_length=2)),
                ('Employee_Id', models.IntegerField()),
                ('Employee_Number', models.IntegerField()),
                ('PAN_Number', models.BigIntegerField(blank=True, null=True)),
                ('Employee_Name_Initials', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Middle_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Full_Name', models.CharField(max_length=100)),
                ('Title', models.CharField(choices=[('1', 'Mr.'), ('2', 'Miss'), ('3', 'Mrs')], max_length=2)),
                ('Date_Of_Birth', models.DateField()),
                ('Date_of_Joined', models.DateField()),
                ('Probation_Period', models.IntegerField(blank=True, null=True)),
                ('Date_Of_Confirmation', models.DateField(blank=True, null=True)),
                ('Date_Of_Resignation', models.DateField(blank=True, null=True)),
                ('Last_Date_Work', models.DateField(blank=True, null=True)),
                ('Designation', models.CharField(max_length=100)),
                ('Salary_Tier', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2, null=True)),
                ('Grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=2, null=True)),
                ('Daily_Attendance_Enable', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('Decided', 'TBD')], max_length=7, null=True)),
                ('TDS_Enable', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('Decided', 'TBD')], max_length=7, null=True)),
                ('PF_Enable', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('Decided', 'TBD')], max_length=7)),
                ('TF_Enable', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('Decided', 'TBD')], max_length=7)),
                ('Staff_Welfare', models.CharField(max_length=7)),
                ('Sports_Fund', models.CharField(max_length=7)),
                ('CSR_Foundation_Fund', models.CharField(max_length=7)),
                ('Staff_Loan_Entitlement', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('Decided', 'TBD')], max_length=7)),
                ('Limit_Loan', models.IntegerField()),
                ('Term_Repayment', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annualy', 'Annualy')], max_length=30)),
                ('LOO_Issued_Date', models.DateField(blank=True, null=True)),
                ('LOA_Issued_Date', models.DateField(blank=True, null=True)),
                ('NDA_Signed_Date', models.DateField(blank=True, null=True)),
                ('Resignation_Recorded_Date', models.DateField()),
                ('Resignation_Approved_Date', models.DateField()),
                ('Service_Letter_Issued_Date', models.DateField()),
                ('Bank_Name_and_Code', models.CharField(blank=True, max_length=500, null=True)),
                ('Bank_Branch_Name_and_Code', models.CharField(blank=True, max_length=500, null=True)),
                ('Bank_Account', models.BigIntegerField()),
                ('Bank_Account_Number', models.BigIntegerField()),
                ('Medical_History', models.CharField(max_length=300)),
                ('Employee_Mobile_Number', models.BigIntegerField()),
                ('Emergency_Relative_Mobile_Number', models.BigIntegerField(blank=True, null=True)),
                ('Emergency_Relative_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Emergency_Relative_Relations', models.CharField(blank=True, max_length=200, null=True)),
                ('Emergency_Blood_Group', models.CharField(blank=True, choices=[('A+', 'A+'), ('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('O-', 'O-'), ('B-', 'B-'), ('AB-', 'AB-')], max_length=4, null=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
            },
        ),
    ]
