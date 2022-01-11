from django.shortcuts import render

# Create your views here.
from rest_framework import filters, generics, viewsets

from api.models import Blog
from api.serializers import BlogSerializer


class BlogInfo(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogSearch(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['blog_title']
    ordering_fields = ['last_updated']
