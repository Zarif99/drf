from django.urls import path, include
from restapi.views import ArticleList, ArticleDetail


urlpatterns = [
    path('article/', ArticleList.as_view(), name='article_list_url'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail_url'),
]