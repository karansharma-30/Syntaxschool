# profile/models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
  

    def __str__(self):
        return self.user.username


class PasswordReset(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"
    