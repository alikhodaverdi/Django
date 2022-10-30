from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize

from .models import Post
from .serlializers import PostSerializer

# Create your views here.


class PostListView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)