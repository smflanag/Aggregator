from django.forms import ModelForm
from django.views.generic import CreateView

from groups.models import Topic


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = ('topic_name', 'topic_description')
