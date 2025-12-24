from django.urls import path
from .views import UserCreateView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='user-create' ),
    path('login', LoginView.as_view(), name='login' ),
    path('logout', LogoutView.as_view(), name='logout' ),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh' ),
    
]