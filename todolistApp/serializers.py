from rest_framework import serializers

from todolistApp.models import Task, Comment, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['task', 'comment']

    def validate_comment(self, value):
        if 'badword' in value:
            raise serializers.ValidationError('Не допустимо писать badword')
        return value


class TaskSerializer(serializers.ModelSerializer):
    tags_count = serializers.IntegerField(source='tags.all.count', read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.all.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        exclude = ['owner']

