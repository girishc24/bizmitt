from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Company, Department, Designation, Tier, Employee
# Register your models here.



admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Tier)
admin.site.register(Employee)
