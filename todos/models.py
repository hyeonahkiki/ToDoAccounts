from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    # settings.AUTH_USER_MODEL 는 User모델을 가르키는 것
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)