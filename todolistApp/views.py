from rest_framework import viewsets, generics, mixins
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from todolistApp.models import Task, Comment, Tag
from todolistApp.serializers import TaskSerializer, CommentSerializer, TagSerializer
from django.http import JsonResponse
from todolist.tasks import add, long_task
from celery.result import AsyncResult


def add_view(request):
    result = add.delay(4, 4)
    return JsonResponse({'task_id': result.id, 'status': 'Task Submitted'})


def long_task_view(request):
    result = long_task.delay()
    return JsonResponse({'task_id': result.id, 'status': 'Long Task Submitted'})


def check_task_status_view(request, task_id):
    result = AsyncResult(task_id)
    if result.state == 'PENDING':
        response = {
            'state': result.state,
            'status': 'Pending...'
        }
    elif result.state != 'FAILURE':
        response = {
            'state': result.state,
            'result': result.result
        }
    else:
        response = {
            'state': result.state,
            'status': str(result.info)  # Ошибка когда-нибудь сохранится в результат
        }
    return JsonResponse(response)


@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagListViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentListViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = TagSerializer


