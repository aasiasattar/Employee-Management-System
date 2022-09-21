from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=100)
    empdept = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)
    

    def __str__(self):
        return self.user.username




class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course_pg = models.CharField(max_length=100,null=True)
    clg_uni_pg = models.CharField(max_length=200,null=True)
    yearofpassing_pg = models.CharField(max_length=20,null=True)
    percentage_pg = models.CharField(max_length=30,null=True)
    course_gra = models.CharField(max_length=100,null=True)
    clg_uni_gra = models.CharField(max_length=200,null=True)
    yearofpassing_gra = models.CharField(max_length=20,null=True)
    percentage_gra = models.CharField(max_length=30,null=True)
    course_ssc = models.CharField(max_length=100,null=True)
    clg_uni_ssc = models.CharField(max_length=200,null=True)
    yearofpassing_ssc = models.CharField(max_length=20,null=True)
    percentage_ssc = models.CharField(max_length=30,null=True)
    course_hsc = models.CharField(max_length=100,null=True)
    clg_uni_hsc = models.CharField(max_length=200,null=True)
    yearofpassing_hsc = models.CharField(max_length=20,null=True)
    percentage_hsc = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.user.username



class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1_name = models.CharField(max_length=100,null=True)
    company1_designation = models.CharField(max_length=100,null=True)
    company1_salary = models.CharField(max_length=100,null=True)
    company1_duration = models.CharField(max_length=100,null=True)
    company2_name = models.CharField(max_length=100,null=True)
    company2_designation = models.CharField(max_length=100,null=True)
    company2_salary = models.CharField(max_length=100,null=True)
    company2_duration = models.CharField(max_length=100,null=True)
    company3_name = models.CharField(max_length=100,null=True)
    company3_designation = models.CharField(max_length=100,null=True)
    company3_salary = models.CharField(max_length=100,null=True)
    company3_duration = models.CharField(max_length=100,null=True)
    
    
    
    def __str__(self):
        return self.user.username
    

    
