from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Article
from django.urls import reverse_lazy
from accounts.models import CustomUser


class ArticleListView(ListView):
    template_name = "articles_list.html"
    model = Article


class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_create.html"
    model = Article
    fields = ("title", "description", "image", "body")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="Jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article_update.html"
    model = Article
    fields = ("title", "description", "image", "body")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="Jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article_delete.html"
    model = Article
    success_url = reverse_lazy("articles_list")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="Jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
