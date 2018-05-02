from toDo.models import ToDoItem
from toDo.serializers import ToDoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    def perform_create(self, serializer):
        # Save instance to get primary key and then update url
        instance = serializer.save()
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        instance.save()

    def delete(self, request):
        ToDoItem.objects.all().delete() # <- This is DANGEROUS
        return Response(status=status.HTTP_204HTTP_204_NO_CONTENT)
