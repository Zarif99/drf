from django.urls import path, include
from restapi.views import ArticleList, ArticleDetail


urlpatterns = [
    path('articles/', ArticleList.as_view({'get':'list'}), name='article_list_url'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail_url'),
]