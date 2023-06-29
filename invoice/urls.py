from django.urls import path,include
from .import views


urlpatterns=[
    path('',views.invoice_list_create_view,name='invoice-list'),
    path('<int:pk>/',views.invoice_detail_view,name='invoice-detail'),
    path('<int:pk>/update/',views.invoice_update_view,name='invoice-update'),
    path('<int:pk>/delete/',views.invoice_delete_view,name='invoice-delete')
]