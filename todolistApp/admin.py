from django.contrib import admin
from todolistApp.models import Task, Comment


# admin.site.register(Task)

class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'due_date')
    list_filter = ('status', 'owner', 'due_date')
    search_fields = ('name', 'description')

    inlines = [CommentInline]