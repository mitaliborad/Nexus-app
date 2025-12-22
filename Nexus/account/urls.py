from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserCreateView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='user-create' ),

]