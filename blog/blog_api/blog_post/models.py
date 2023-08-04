from django.db import models
from blog_api.category.models import Category

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	author = models.CharField(max_length=50, null=True, blank=True)
	image = models.ImageField(null=True, blank=True, upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.title