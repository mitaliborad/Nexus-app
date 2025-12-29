from django.db import models
from account.models import User
from post.models import Post

# Create your models here.

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.user_id.email} on Post ID {self.post_id.id}'
    


