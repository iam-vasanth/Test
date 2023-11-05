from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    task=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.task}'

    class Meta:
         get_latest_by = 'created_at'