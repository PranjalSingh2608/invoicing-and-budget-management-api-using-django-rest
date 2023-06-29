from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    def total_expenses(self):
        return self.expenses.aggregate(total=models.Sum('amount')).get('total') or 0

    def __str__(self):
        return self.name

class Expense(models.Model):
    name=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='expenses')

    def __str__(self):
        return self.name