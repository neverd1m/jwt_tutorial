from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    user = serializers.ReadOnlyField(source='user.username')
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ['created_at', 'updated_at', 'title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like_post(self, request, pk=None):
        post = self.get_object()
        profile = Profile.objects.get(user=request.user)
        profile.liked_posts.add(post)
        profile.save()
        post.recount_likes()
        return Response({'status': 'Добавлен лайк'})

    @action(detail=True, methods=['post'])
    def unlike_post(self, request, pk=None):
        post = self.get_object()
        profile = Profile.objects.get(user=request.user)
        profile.liked_posts.remove(post)
        profile.save()
        post.recount_likes()
        return Response({'status': 'Убран лайк'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering_fields = ['username']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    ordering_fields = ['last_login', 'last_request']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
