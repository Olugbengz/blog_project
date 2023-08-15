from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
	name = models.CharField(max_length=50, default='Anonymous')
	email = models.EmailField(max_length=150, unique=True)

	username = None

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	session_token = models.CharField(max_length=10, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)