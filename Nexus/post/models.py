from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    caption = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='media_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.email} at {self.uploaded_at}'
    
class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user_id.email} on Post ID {self.post_id.id}'

    


