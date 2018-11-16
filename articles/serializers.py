from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import UserProfile
from articles.models import Comment, Article
from groups.serializers import TopicSerializer


class VotesSerializer(serializers.Serializer):
    article_id = serializers.CharField(required=True, max_length=200)
    vote_count = serializers.CharField(required=True, max_length=200)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','id')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('user','id')


class CommentsSerializer(serializers.ModelSerializer):
    commenter = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('commenter', 'article', 'comment_body', 'time')


class ArticleSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('created_by','created_at','article_name','topic',)

