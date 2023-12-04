from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class UserFollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    followings = UserFollowSerializer(many=True, read_only=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)
    followers = UserFollowSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'followings', 'followers', 'following_count', 'follower_count',)