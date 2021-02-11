# django
from django.shortcuts import get_object_or_404
# rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# app
from restapi.models import Article
from restapi.serializers import ArticleSerializer


class ArticleList(APIView):
    def get(self, request):
        articles = get_object_or_404(Article, draft=False)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk, draft=False)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk, draft=False)
        serializer = ArticleSerializer(article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
