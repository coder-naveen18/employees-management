from django.db import models

# Create your models here.
class Employees_detail( models.Model ):
     name = models.CharField( max_length=100)
     email_id = models.EmailField(max_length=254, unique = True)
     phone_no = models.CharField(max_length=10)
     designation = models.CharField(max_length=100)
     image = models.ImageField(upload_to='images/')
       
     def __str__(self):
          return self.name
        
       