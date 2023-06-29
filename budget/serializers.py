from rest_framework import serializers
from .models import Category,Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    expenses=ExpenseSerializer(many=True,read_only=True)
    total_expenses=serializers.ReadOnlyField()

    class Meta:
        model=Category
        fields=['id','name','expenses','total_expenses']