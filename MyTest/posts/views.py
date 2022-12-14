from django.http import Http404

from http.client import BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize

from .models import Post
from .serlializers import PostSerializer

# Create your views here.


class PostListView(APIView):
    
    def get_object(self,post_id):
        try: 
            post = Post.objects.get(pk =post_id)
        except Post.DoesNotExist:
            raise Http404
        return post
    
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=BAD_REQUEST)
    
    def put(self, request ,post_id):
        post  =self.get_object(post_id)
        serializer = PostSerializer(post ,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=BAD_REQUEST)
    
   

    
class PostDetailView(APIView):
   
    def get_object(self,post_id):
        try: 
            post = Post.objects.get(pk =post_id)
        except Post.DoesNotExist:
            raise Http404
        return post
    
    def get(self,request ,post_id):
        post  =self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def delete(self,request,post_id):
        post = self.get_object(post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    