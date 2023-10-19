from rest_framework import serializers
from .models import Music,Comment


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class MusicTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ('title',)

    music = MusicTitleSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'