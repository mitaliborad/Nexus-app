from django.urls import path
from .views import UserCreateView, LoginView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='user-create' ),
    path('login', LoginView.as_view(), name='login' ),
    
]