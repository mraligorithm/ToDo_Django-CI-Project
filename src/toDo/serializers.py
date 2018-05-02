from rest_framework import serializers
from toDo.models import ToDoItem

class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = ToDoItem
        fields = ('url', 'title', 'completed', 'order')
