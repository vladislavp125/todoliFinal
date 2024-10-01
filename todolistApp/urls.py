from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolistApp.views import TodolistViewSet, CommentListCreateAPIView, CommentUpdateDestroyRetrieveAPIView, \
    TagListViewSet, TaskCreateView, TaskDestroyView, TaskUpdateView, TaskRetrieveView, TaskListView, TaskListView, \
    CommentCreateView, CommentListView, CommentRetrieveView, CommentUpdateView, CommentDestroyView, TagCreateView, \
    TagListView, TagRetrieveView, TagUpdateView, TagDestroyView

app_name = 'tasks'


router = DefaultRouter()
router.register('tasks', TodolistViewSet)
router.register('tags', TagListViewSet)

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDestroyView.as_view(), name='task-destroy'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='comment-retrieve'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagRetrieveView.as_view(), name='tag-retrieve'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDestroyView.as_view(), name='tag-destroy'),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('', include(router.urls)),
    path('comments/<int:pk>/', CommentUpdateDestroyRetrieveAPIView.as_view())
] + router.urls