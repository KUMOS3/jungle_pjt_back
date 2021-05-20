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

class ReviewSerializer(serializers.ModelSerializer):
    # article과 연결되어있는 comment들을 다 가져온다.
    # 사용자에게 정보를 받는게 목적이 아니므로 is_valid통과 위해 read_only옵션 설정
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  
    comments = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 숫자로 변환해서 저장해주는 필드
    class Meta():
        model = Review
        fields = '__all__'
