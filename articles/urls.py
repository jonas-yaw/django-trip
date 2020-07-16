from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("new", ArticleCreateView.as_view(), name="article_create"),
    path("<slug:slug>/edit", ArticleUpdateView.as_view(), name="article_update"),
    path("<slug:slug>/delete", ArticleDeleteView.as_view(), name="article_delete"),
]
