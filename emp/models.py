from django.db import models

# Create your models here.

class Emp(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    emp_age = models.CharField(max_length=10)  
    emp_phone_no = models.CharField(max_length=10)
    emp_address = models.CharField(max_length=150)
    emp_working = models.BooleanField(default=True)
    emp_department = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.name
      
        

