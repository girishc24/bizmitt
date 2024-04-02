from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    business= models.CharField(max_length=200, unique=True, null = False)
    email = models.CharField(max_length=200, unique=True, null = False)
    phoneno = models.CharField(max_length=12, unique=True, null = False)
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