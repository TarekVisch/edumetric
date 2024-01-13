from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('teacher', 'Teacher')])

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)