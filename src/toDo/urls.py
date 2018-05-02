from django.conf.urls import url, include
from toDo import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it
router = DefaultRouter(trailing_slash=False)
router.register(r'toDos', views.ToDoItemViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    url(r'^', include(router.urls)),
]
