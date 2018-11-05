from rest_framework import serializers
from .models import Article, Vote


class VotesSerializer(serializers.Serializer):
    article_id = serializers.CharField(required=True, max_length=200)
    vote_count = serializers.CharField(required=True, max_length=200)
