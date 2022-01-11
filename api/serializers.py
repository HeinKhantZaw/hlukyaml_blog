from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'blog_title', 'blog_cover', 'blog_body', 'author', 'last_updated')


