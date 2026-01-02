from django.urls import path
from .views import CommentCreateReadView, CommentUpdateDeleteView

urlpatterns = [
    path('create/', CommentCreateReadView.as_view(), name='comment-create' ),
    path('update-delete/<int:id>/', CommentUpdateDeleteView.as_view(), name='update-delete-comment' )
]
