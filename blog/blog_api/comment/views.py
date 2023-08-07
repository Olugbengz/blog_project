from django.shortcuts import render
from .models import Comment
from rest_framework import viewsets
from .serializers import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all().order_by('post')
	serializer_class = CommentSerializer