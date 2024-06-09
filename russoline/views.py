from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import ContentSerializer, ContentUploadSerializer, ProfileSerializer, SingleContentSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated
from .models import Content, Like, Follow, Comment

from users.models import User
    

#Page APIs    

class IndexAPI(APIView):
    def get(self,request):
        posts = Content.objects.all().order_by('created_at')
        serializer = ContentSerializer(posts,many=True)
        return Response(serializer.data)
    
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = get_object_or_404(User,pk=request.user.id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    
class UploadContentAPI(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self,request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ContentUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
class SingleContentAPI(APIView):
    def get(self,request,id):
        content = get_object_or_404(Content,pk=id)
        serializer = SingleContentSerializer(content)
        return Response(serializer.data)
    
    def delete(self,request,id):
        content = get_object_or_404(Content,pk=id)
        content.delete()
        return Response({"status":True,"msg":"Deleted successfully"})
    
class CommentAPI(APIView):
    def post(self,reuqest):
        data = reuqest.data.copy()
        data["user"] = reuqest.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":True,"msg":"commented"})
        return Response(serializer.errors)

class CommentEditAPI(APIView):
    def delete(self,request,id):
        comment = get_object_or_404(pk=id)
        comment.delete()
        return Response({"status":True,"msg":"comment deleted"})
    
#Action APIs

def like(request,content):
    Like.objects.create(
        user = request.user,
        content = content
    )
    return Response({"status":True,"msg":"Action like"})

def follow(request,creator):
    Follow.objects.create(
        follower = request.user,
        channel = creator
    )
    return Response({"status":True,"msg":"Action subscribe"})