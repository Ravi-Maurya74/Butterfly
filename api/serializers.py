from rest_framework import serializers
from .models import ApiUser, Post, Reply


class IdentifyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = [
            'id',
            'user_email',
            'password',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'user_email',
            'following',
            'followers',
            'user_posts',
            'dob',
            'bookmarked_posts',
        ]


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUser
        fields = [
            'first_name',
            'last_name',
            'user_email',
            'password',
            'dob',
        ]


class PostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user_id',
            'content',
            'created',
            'liked_by',
            'bookmarked_by',
            'replies',
        ]


class PostIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
        ]


class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user_id',
            'content',
        ]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            'replied_to',
            'content',
        ]
