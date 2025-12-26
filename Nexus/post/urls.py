from django.urls import path
from .views import PostCreateReadView, PostUpdateDeleteView

urlpatterns = [
    path('create/', PostCreateReadView.as_view(), name='post-create'),
    path('feed/', PostCreateReadView.as_view(), name='post-list'),
    path('update-delete/<int:id>/', PostUpdateDeleteView.as_view(), name='post-update-delete'),
]