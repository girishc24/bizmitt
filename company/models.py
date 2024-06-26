from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    business= models.CharField(max_length=200, unique=True, null = False)
    email = models.CharField(max_length=200, unique=True, null = False)
    gstno = models.CharField(max_length=12, unique=True, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=50)



    def __str__(self) -> str:
        return self.business

    """def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        self.user.created_at = self.created_at
        self.user.save()"""
    
class Department(models.Model):
    cno = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    department = models.CharField(max_length=200, unique=True, null = False)

    def __str__(self) -> str:
        return (f"{self.department}")

class Designation(models.Model):
    cno = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="companyname")
    dno = models.ForeignKey(Department, on_delete=models.CASCADE )
    designation = models.CharField(max_length=200, unique=True, null = False)

    def __str__(self) -> str:
        return (f"{self.designation}")

class Tier(models.Model):
    cno = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="companytier")
    tier = models.CharField(max_length=200, unique=True, null = False)

    def __str__(self) -> str:
        return (f"{self.tier}")
    
class Reimbursementlist(models.Model):
    cno = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="reimbursementcno")
    list = models.CharField(max_length=200, unique=True, null = False)

    def __str__(self) -> str:
        return (f"{self.list}")    
   

class Employee(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    cno = models.ForeignKey(Company, on_delete=models.CASCADE)
    employeename  = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=10, unique=True, null=False)
    email = models.CharField(max_length=200, unique=True, null=False)
    officalemail = models.CharField(max_length=200, unique=True)
    department = models.OneToOneField(Department, on_delete=models.PROTECT)
    designation = models.OneToOneField(Designation, on_delete=models.PROTECT)
    tier = models.OneToOneField(Tier, on_delete=models.PROTECT)
    password = models.CharField(max_length=50)