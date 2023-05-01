from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =50)
    location = models.CharField(max_length =50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'),
                                                    ('Non IT',"Non IT"),
                                                    ('Mobiles Phones','Mobiles Phones')
                                                    ))
    added_date = models.DateTimeField(auto_now =True)
    activate = models.BooleanField(default=True)



class Employee(models.Model):
    emp_name =models.CharField(max_length=100)
    emp_email = models.CharField(max_length=50)
    emp_address = models.CharField(max_length=200)
    emp_phone = models.CharField(max_length=10)
    emp_about = models.TextField()
    emp_position = models.CharField(max_length=50, choices=(('Manager','Manager'),
                                                            ('Software Developer','Software Developer'),
                                                            ('Project Leader','Project Leader')
                                                            ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)





