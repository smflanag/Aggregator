from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import UserProfile, Contact
from articles.models import Comment, Article
from groups.models import Topic


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



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user



class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','topic_name','topic_description','slug','members')


class ArticleSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('created_by','created_at','article_name','topic', 'id')

class ArticleSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_name','id')

class CommentsSerializer(serializers.ModelSerializer):
    commenter = UserProfileSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('commenter', 'article', 'comment_body', 'time', 'id')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name','email', 'feedback')