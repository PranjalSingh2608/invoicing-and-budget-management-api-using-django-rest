from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    def total_expenses(self):
        return self.expenses.aggregate(total=models.Sum('amount')).get('total') or 0

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User,default=1, null=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='expenses')

    def __str__(self):
        return self.name