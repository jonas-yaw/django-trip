from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleAndCommentView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path("new/", ArticleCreateView.as_view(), name="article_create"),
    path("<slug:slug>/", ArticleAndCommentView.as_view(), name="article_detail"),
    path("<slug:slug>/edit", ArticleUpdateView.as_view(), name="article_update"),
    path("<slug:slug>/delete", ArticleDeleteView.as_view(), name="article_delete"),
]
