from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['name',   'comment']