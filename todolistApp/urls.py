from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolistApp.views import TodolistViewSet, CommentListCreateAPIView, CommentUpdateDestroyRetrieveAPIView, \
    TagListViewSet

app_name = 'tasks'


router = DefaultRouter()
router.register('tasks', TodolistViewSet)
router.register('tags', TagListViewSet)

urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('comments/<int:pk>/', CommentUpdateDestroyRetrieveAPIView.as_view())
] + router.urls