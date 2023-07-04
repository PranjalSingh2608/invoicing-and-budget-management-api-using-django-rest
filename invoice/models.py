from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Client(models.Model):
    full_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.BigIntegerField()
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    def __str__(self):
        return self.name

    
class Invoice(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    invoice_number=models.CharField(max_length=100)
    issue_date=models.DateField()
    due_date=models.DateField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    item_description=models.CharField(max_length=200)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,related_name='invoices')
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='invoices')

    def __str__(self):
        return self.invoice_number
    


