from django.urls import path
from .views import PostCreateReadView

urlpatterns = [
    path('create/', PostCreateReadView.as_view(), name='post-create'),
]