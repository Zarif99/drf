# django
from django.shortcuts import get_object_or_404
# rest_framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# app
from restapi.models import Article
from restapi.serializers import ArticleSerializer


class ArticleList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleSerializer


class ArticleDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
