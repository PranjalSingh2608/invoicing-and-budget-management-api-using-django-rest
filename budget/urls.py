from django.urls import path,include
from .import views


urlpatterns=[    
    path('category/',views.category_list_create_view,name='category-list'),
    path('category/<int:pk>/',views.category_alter_view,name='category-alter'),
    path('expense/',views.expense_list_create_view,name='expense-list'),
    path('expense/<int:pk>/',views.expense_alter_view,name='expense-alter'),
]