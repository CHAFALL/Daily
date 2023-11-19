from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Comment , Review
from . serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def review_list_create(request) :
    if request.method == 'GET' :
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# Detail에 대한 get 집어넣기.

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE' :
        if not request.user.review_set.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)
        review.delete()
        return Response({ 'id': review_pk}, status=status.HTTP_204_NO_CONTENT)

# 해당 리뷰에 대한 comment 생성 및 조회
@api_view(['GET','POST'])
def comment_list_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method =='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 comment 조회, 수정 및 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            # 아래를 보면 comment 인스턴스에 이미 movie 데이터가 있어서 review을 넘겨주지 않아도 됨을 알 수 있다.
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
