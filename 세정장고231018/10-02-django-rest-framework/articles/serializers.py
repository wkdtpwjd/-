from rest_framework import serializers
from .models import Article,Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)



class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # override 
    article = ArticleSerializer(read_only=True) 


    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)




class ArticleSerializer(serializers.ModelSerializer):  # 이거 조회할때 댓글도 같이 조회하고 싶음.....
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(read_only=True,source='comment_set.count')
    class Meta:
        model = Article
        fields = '__all__'
