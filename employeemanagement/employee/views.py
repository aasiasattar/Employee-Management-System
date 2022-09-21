from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email'] 
        p = request.POST['pwd'] 
        try:
            user =  User.objects.create_user(first_name=fn,last_name=ln,username=em,password=p)
            EmployeeDetail.objects.create(user=user,empcode=ec)
            EmployeeEducation.objects.create(user=user)
            EmployeeExperience.objects.create(user=user)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'registration.html',locals())



def emp_login(request):
    Error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
               login(request,user)
               error = "no"
        else:
               error = "yes"
            
    return render(request, 'emp_login.html',locals())





def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')



def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dep = request.POST['department']
        des = request.POST['designation']
        con = request.POST['contact']
        jd = request.POST['jdate'] 
        g = request.POST['gender'] 


        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dep
        employee.designation = des
        employee.contact = con
        employee.gender = g

        if jd:
            employee.joiningdate = jd
        try:
            employee.user.save()
            employee.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'profile.html',locals())


def admin_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            error = "no"
        else:
            error = "yes"

    return render(request,'admin_login.html',locals())



def Logout(request):
    logout(request)
    return redirect('index')



def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    
    return render(request, 'myexperience.html',locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        n1 = request.POST['name1']
        jd1 = request.POST['jobdesignation1']
        js1 = request.POST['jobsalary1']
        jdur1 = request.POST['jobduration1']
        n2 = request.POST['name2']
        jd2 = request.POST['jobdesignation2']
        js2 = request.POST['jobsalary2']
        jdur2 = request.POST['jobduration2']
        n3 = request.POST['name3']
        jd3 = request.POST['jobdesignation3']
        js3 = request.POST['jobsalary3']
        jdur3 = request.POST['jobduration3']



        experience.company1_name = n1
        experience.company1_designation = jd1
        experience.company1_salary = js1
        experience.company1_duration = jdur1
        experience.company2_name = n2
        experience.company2_designation = jd2
        experience.company2_salary = js2
        experience.company2_duration = jdur2
        experience.company3_name = n3
        experience.company3_designation = jd3
        experience.company3_salary = js3
        experience.company3_duration = jdur3


        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'edit_experience.html',locals())





def myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    return render(request,'myeducation.html', locals())





def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        cp = request.POST['course_pg']
        cup = request.POST['clg_uni_pg']
        ypp = request.POST['yearofpassing_pg']
        percent1 = request.POST['percentage_pg']

        cg = request.POST['course_gra']
        cug = request.POST['clg_uni_gra']
        ypg = request.POST['yearofpassing_gra']
        percent2 = request.POST['percentage_gra']

        cs = request.POST['course_ssc']
        cus = request.POST['clg_uni_ssc']
        yps = request.POST['yearofpassing_ssc']
        percent3 = request.POST['percentage_ssc']


        ch = request.POST['course_hsc']
        cuh = request.POST['clg_uni_hsc']
        yph = request.POST['yearofpassing_hsc']
        percent4 = request.POST['percentage_hsc']



        education.course_pg = cp
        education.clg_uni_pg = cup
        education.yearofpassing_pg= ypp
        education.percentage_pg = percent1

        education.course_gra = cg
        education.clg_uni_gra = cug
        education.yearofpassing_gra= ypg
        education.percentage_gra = percent2


        education.course_ssc = cs
        education.clg_uni_ssc = cus
        education.yearofpassing_ssc = yps
        education.percentage_ssc = percent3


        education.course_hsc = ch
        education.clg_uni_hsc = cuh
        education.yearofpassing_hsc= yph
        education.percentage_hsc = percent4




        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'edit_education.html',locals())





def emp_change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
        
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
                
        except:
            error = "yes"

    
    return render(request,'emp_change_password.html',locals())




def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')



def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    user = request.user
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        try:
        
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
                
        except:
            error = "yes"

    
    return render(request,'admin_change_password.html',locals())



def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request,'all_employee.html',locals())



def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')
    





def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    
    employee = EmployeeDetail.objects.get(id=pid)
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dep = request.POST['department']
        des = request.POST['designation']
        con = request.POST['contact']
        jd = request.POST['jdate'] 
        g = request.POST['gender'] 


        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dep
        employee.designation = des
        employee.contact = con
        employee.gender = g

        if jd:
            employee.joiningdate = jd
        try:
            employee.user.save()
            employee.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'edit_profile.html',locals())



def admin_edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        cp = request.POST['course_pg']
        cup = request.POST['clg_uni_pg']
        ypp = request.POST['yearofpassing_pg']
        percent1 = request.POST['percentage_pg']

        cg = request.POST['course_gra']
        cug = request.POST['clg_uni_gra']
        ypg = request.POST['yearofpassing_gra']
        percent2 = request.POST['percentage_gra']

        cs = request.POST['course_ssc']
        cus = request.POST['clg_uni_ssc']
        yps = request.POST['yearofpassing_ssc']
        percent3 = request.POST['percentage_ssc']


        ch = request.POST['course_hsc']
        cuh = request.POST['clg_uni_hsc']
        yph = request.POST['yearofpassing_hsc']
        percent4 = request.POST['percentage_hsc']



        education.course_pg = cp
        education.clg_uni_pg = cup
        education.yearofpassing_pg= ypp
        education.percentage_pg = percent1

        education.course_gra = cg
        education.clg_uni_gra = cug
        education.yearofpassing_gra= ypg
        education.percentage_gra = percent2


        education.course_ssc = cs
        education.clg_uni_ssc = cus
        education.yearofpassing_ssc = yps
        education.percentage_ssc = percent3


        education.course_hsc = ch
        education.clg_uni_hsc = cuh
        education.yearofpassing_hsc= yph
        education.percentage_hsc = percent4




        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'admin_edit_education.html',locals())




def admin_edit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
        n1 = request.POST['name1']
        jd1 = request.POST['jobdesignation1']
        js1 = request.POST['jobsalary1']
        jdur1 = request.POST['jobduration1']
        n2 = request.POST['name2']
        jd2 = request.POST['jobdesignation2']
        js2 = request.POST['jobsalary2']
        jdur2 = request.POST['jobduration2']
        n3 = request.POST['name3']
        jd3 = request.POST['jobdesignation3']
        js3 = request.POST['jobsalary3']
        jdur3 = request.POST['jobduration3']



        experience.company1_name = n1
        experience.company1_designation = jd1
        experience.company1_salary = js1
        experience.company1_duration = jdur1
        experience.company2_name = n2
        experience.company2_designation = jd2
        experience.company2_salary = js2
        experience.company2_duration = jdur2
        experience.company3_name = n3
        experience.company3_designation = jd3
        experience.company3_salary = js3
        experience.company3_duration = jdur3


        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}

    return render(request, 'admin_edit_experience.html',locals())







    






