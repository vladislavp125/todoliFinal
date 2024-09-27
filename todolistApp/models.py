from django.db import models


class Task(models.Model):
    STATUS_DRAFT = 'DRAFT'
    STATUS_PUBLISHED = 'PUBLISHED'

    STATUSES = (
        ('DRAFT', 'Черновик'),
        ('PUBLISHED', 'Опубликовано'),
    )

    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    tags = models.ManyToManyField('todolistApp.Tag', related_name='tasks', verbose_name='Теги')

    status = models.CharField(choices=STATUSES, default=STATUS_DRAFT, verbose_name='Статус', max_length=10)
    owner = models.CharField(max_length=50, default='anonim', verbose_name='Владелец')

    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Дедлайн')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')

    comment = models.CharField(max_length=255, verbose_name='Коментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.comment


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name