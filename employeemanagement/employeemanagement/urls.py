"""employeemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registration', registration, name="registration"),
    path('emp_login', emp_login, name="emp_login"),
    path('emp_home', emp_home, name="emp_home"),
    path('profile', profile, name="profile"),
    path('Logout', Logout, name="Logout"),
    path('admin_login', admin_login, name="admin_login"),
    path('myexperience', myexperience, name="myexperience"),
    path('edit_experience', edit_experience, name="edit_experience"),
    path('myeducation', myeducation, name="myeducation"),
    path('edit_education', edit_education, name="edit_education"),
    path('emp_change_password', emp_change_password, name="emp_change_password"),
    path('admin_home', admin_home, name="admin_home"),
    path('admin_change_password', admin_change_password, name="admin_change_password"),
    path('all_employee', all_employee, name="all_employee"),
    path('delete_employee/<int:pid>', delete_employee, name="delete_employee"),
    path('edit_profile/<int:pid>', edit_profile, name="edit_profile"),
    path('admin_edit_education/<int:pid>', admin_edit_education, name="admin_edit_education"),
    path('admin_edit_experience/<int:pid>', admin_edit_experience, name="admin_edit_experience"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
