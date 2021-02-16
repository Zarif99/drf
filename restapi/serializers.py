from rest_framework import serializers

from restapi.models import Article, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        include = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('draft',)















    # title = serializers.CharField(max_length=255)
    # author = serializers.CharField(max_length=255)
    # email = serializers.EmailField(max_length=100)
    # date_pub = serializers.DateTimeField()
    # date_update = serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.date_pub = validated_data.get('date_pub', instance.date_pub)
    #     instance.date_update = validated_data.get('date_update', instance.date_update)
    #     instance.save()
    #     return instance
