from rest_framework import generics

from blog.models import Post
from blog.api.serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class PostView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
