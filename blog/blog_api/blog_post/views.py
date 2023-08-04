from django.shortcuts import render
from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializer

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all().order_by('created_at')
	serializer_class = BlogSerializer