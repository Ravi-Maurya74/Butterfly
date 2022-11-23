from django.shortcuts import render
from rest_framework import generics
from .models import ApiUser, Post, Reply
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.db.models import Q
from .serializers import IdentifyUserSerializer, UserDetailSerializer, NewUserSerializer, PostInfoSerializer, \
    PostIdSerializer, NewPostSerializer, ReplySerializer


# Create your views here.

class IdentifyUserApi(generics.RetrieveAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = IdentifyUserSerializer


class UserDetailApi(generics.RetrieveAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = UserDetailSerializer


class NewUserApi(generics.CreateAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = NewUserSerializer


class IdentifyUserEmailApi(generics.RetrieveAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = IdentifyUserSerializer
    lookup_field = 'user_email'


class GetAllUsersApi(generics.ListAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = UserDetailSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostInfoSerializer


@api_view(['POST'])
def homePagePosts(request):
    received_json_data = json.loads(request.body)
    user_ids = list(received_json_data['following'])
    queryset = Post.objects.filter(user_id__in=user_ids)
    data = PostIdSerializer(queryset, many=True).data
    return Response(data)


@api_view(['POST'])
def likePost(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    post = Post.objects.get(pk=received_json_data['post_id'])
    user.liked_posts.add(post)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


@api_view(['POST'])
def dislikePost(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    post = Post.objects.get(pk=received_json_data['post_id'])
    user.liked_posts.remove(post)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


class NewPostApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = NewPostSerializer


@api_view(['POST'])
def bookmarkPost(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    post = Post.objects.get(pk=received_json_data['post_id'])
    user.bookmarked_posts.add(post)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


@api_view(['POST'])
def unmarkPost(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    post = Post.objects.get(pk=received_json_data['post_id'])
    user.bookmarked_posts.remove(post)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


@api_view(['POST'])
def followuser(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    to_follow = ApiUser.objects.get(pk=received_json_data['to_follow'])
    user.following.add(to_follow)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


@api_view(['POST'])
def unfollowuser(request):
    received_json_data = json.loads(request.body)
    user = ApiUser.objects.get(pk=received_json_data['user_id'])
    to_unfollow = ApiUser.objects.get(pk=received_json_data['to_unfollow'])
    user.following.remove(to_unfollow)
    user.save()
    data = UserDetailSerializer(user).data
    return Response(data)


@api_view(['POST'])
def search_user(request):
    received_json_data = json.loads(request.body)
    search = received_json_data['name']
    user = ApiUser.objects.filter(
        Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(user_email__icontains=search))
    data = UserDetailSerializer(user, many=True).data
    return Response(data)


class NewReplyApi(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class DeletePostApi(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostIdSerializer


@api_view(['POST'])
def getpostreplies(request):
    received_json_data = json.loads(request.body)
    replies = Reply.objects.filter(replied_to=received_json_data['post_id'])
    data = ReplySerializer(replies, many=True).data
    return Response(data)
