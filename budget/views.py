from rest_framework import generics,permissions
from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='post',
)




class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

category_list_create_view=CategoryListCreateAPIView.as_view()

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =(permissions.IsAuthenticated,)

category_alter_view=CategoryRetrieveUpdateDestroyAPIView.as_view()



class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes =(permissions.IsAuthenticated,)

expense_list_create_view=ExpenseListCreateAPIView.as_view()

class ExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated,)

expense_alter_view=ExpenseRetrieveUpdateDestroyAPIView.as_view()

