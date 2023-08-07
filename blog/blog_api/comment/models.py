from django.db import models
from blog_api.blog_post.models import Blog

# Create your models here.

class Comment(models.Model):
	name = models.CharField(max_length=50)
	post = models.ForeignKey(Blog, on_delete=models.CASCADE)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

