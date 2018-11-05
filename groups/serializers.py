from rest_framework import serializers
from .models import Topic, User


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'topic_name', 'topic_description', 'slug')
