from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolistApp.views import TodolistViewSet, TagListViewSet, CommentListViewSet

app_name = 'tasks'


router = DefaultRouter()
router.register('tasks', TodolistViewSet)
router.register('tags', TagListViewSet)
router.register('comment', CommentListViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + router.urls