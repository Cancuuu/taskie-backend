# Generated by Django 3.2.4 on 2021-11-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=50)),
                ('DepartmentColor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=150)),
                ('Department', models.CharField(max_length=150)),
                ('DateOfJoining', models.DateField()),
            ],
        ),
    ]
