from rest_framework import serializers
from .models import Topic, User


class TopicListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    topic_name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField(),min_length=None,max_length=None)
    articles = serializers.IntegerField()