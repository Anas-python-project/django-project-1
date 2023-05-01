from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    task= models.CharField(max_length=500)
    # user_id= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    note = models.CharField(max_length=20,null=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    completed= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at','-updated_at'] # reverse order or data