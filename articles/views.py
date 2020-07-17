from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Article
from django.urls import reverse_lazy


class ArticleListView(ListView):
    template_name = "articles_list.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article


class ArticleCreateView(CreateView):
    template_name = "article_create.html"
    model = Article
    fields = ("title", "description", "image", "body")
    success_url = reverse_lazy("articles_list")


class ArticleUpdateView(UpdateView):
    template_name = "article_update.html"
    model = Article
    fields = ("title", "description", "image", "body")


class ArticleDeleteView(DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("articles_list")

