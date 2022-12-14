# Generated by Django 4.0 on 2022-01-01 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1_name', models.CharField(max_length=100, null=True)),
                ('company1_designation', models.CharField(max_length=100, null=True)),
                ('company1_salary', models.CharField(max_length=100, null=True)),
                ('company1_duration', models.CharField(max_length=100, null=True)),
                ('company2_name', models.CharField(max_length=100, null=True)),
                ('company2_designation', models.CharField(max_length=100, null=True)),
                ('company2_salary', models.CharField(max_length=100, null=True)),
                ('company2_duration', models.CharField(max_length=100, null=True)),
                ('company3_name', models.CharField(max_length=100, null=True)),
                ('company3_designation', models.CharField(max_length=100, null=True)),
                ('company3_salary', models.CharField(max_length=100, null=True)),
                ('company3_duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_pg', models.CharField(max_length=100, null=True)),
                ('clg_uni_pg', models.CharField(max_length=200, null=True)),
                ('yearofpassing_pg', models.CharField(max_length=20, null=True)),
                ('percentage_pg', models.CharField(max_length=30, null=True)),
                ('course_gra', models.CharField(max_length=100, null=True)),
                ('clg_uni_gra', models.CharField(max_length=200, null=True)),
                ('yearofpassing_gra', models.CharField(max_length=20, null=True)),
                ('percentage_gra', models.CharField(max_length=30, null=True)),
                ('course_ssc', models.CharField(max_length=100, null=True)),
                ('clg_uni_ssc', models.CharField(max_length=200, null=True)),
                ('yearofpassing_ssc', models.CharField(max_length=20, null=True)),
                ('percentage_ssc', models.CharField(max_length=30, null=True)),
                ('course_hsc', models.CharField(max_length=100, null=True)),
                ('clg_uni_hsc', models.CharField(max_length=200, null=True)),
                ('yearofpassing_hsc', models.CharField(max_length=20, null=True)),
                ('percentage_hsc', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
