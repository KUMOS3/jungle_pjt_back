from rest_framework import serializers
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class ReviewSerializer(serializers.ModelSerializer):
    # article과 연결되어있는 comment들을 다 가져온다.
    # 사용자에게 정보를 받는게 목적이 아니므로 is_valid통과 위해 read_only옵션 설정
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  
    comments = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 숫자로 변환해서 저장해주는 필드
    class Meta():
        model = Review
        fields = '__all__'
        read_only_fields = ('review_like_users',)

# 리뷰 좋아요 후 response하는 serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        # 추후 업적 시스템에 활용할 데이터들
        fields = '__all__'

