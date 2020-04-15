from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=30)

    def __str__(self):
        return "Hello World"
        
class Employee(models.Model): 
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    entry_date = models.DateField(auto_now=True)
    leave_date = models.DateField(blank=True)
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    department = models.OneToOneField(
        Department,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return "First Name: %s Last Nmae: %s" % (self.first_name, self.last_name) 


    
    