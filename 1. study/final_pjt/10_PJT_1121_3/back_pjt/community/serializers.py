from rest_framework import serializers
from .models import Review, Comment



class ReviewListSerializer(serializers.ModelSerializer):
    
    # ForeignKey로 연결된 모델의 필드를 가져오기 위해 source 사용
    user_name = serializers.CharField(source='user.username', read_only=True)


    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'user_name', 'rank', 'movie_title')
        


class ReviewSerializer(serializers.ModelSerializer):
    
    # 유저 이름을 가져오기 위해 serializers.SerializerMethodField를 사용
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'user_name', 'like_users',)

    # SerializerMethodField에 대한 메소드 정의
    def get_user_name(self, obj):
        return obj.user.username if obj.user else None


class CommentSerializer(serializers.ModelSerializer):
    
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at','updated_at', 'user_name')
        read_only_fields = ('review', 'user')
        