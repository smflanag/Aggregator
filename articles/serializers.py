from rest_framework import serializers
from articles.models import Comment


class VotesSerializer(serializers.Serializer):
    article_id = serializers.CharField(required=True, max_length=200)
    vote_count = serializers.CharField(required=True, max_length=200)

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('commenter', 'article', 'comment_body')
    # commenter = serializers.CharField(required=True, max_length=200)
    # article_id = serializers.CharField(required=True, max_length=200)
    # comment_body = serializers.CharField(required=True, max_length=200)