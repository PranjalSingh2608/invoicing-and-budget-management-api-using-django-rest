from django.urls import path
from .views import UserCreateAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='signup'),
    path('token/', CustomTokenObtainPairView.as_view(), name='login'),
]