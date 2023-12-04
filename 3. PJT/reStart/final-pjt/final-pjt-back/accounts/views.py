from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_followers(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'POST':
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
            is_follow = False
        else:
            user.followers.add(request.user)
            is_follow = True
        context = {
            'isFollow': is_follow,
            'followerCount': user.followers.count(),
        }
        return JsonResponse(context)

