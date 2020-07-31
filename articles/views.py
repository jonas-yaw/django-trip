from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from accounts.models import CustomUser
from .models import Article, Comment


class ArticleListView(ListView):
    template_name = "articles_list.html"
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_create.html"
    model = Article
    fields = ("title", "description", "body")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != CustomUser.objects.get(username="Jonas"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article_update.html"
    model = Article
    fields = ("title", "description", "body")

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


class ArticleAndCommentView(CreateView):
    template_name = "article_detail.html"
    model = Comment
    fields = ("comment",)

    def form_valid(self, form):
        if self.request.user.is_anonymous:
            return redirect("login")
        else:
            form.instance.author = self.request.user
            article_path_to_array = self.request.path.strip("/").split("/")
            article_slug = article_path_to_array[1]
            form.instance.article = Article.objects.get(slug=article_slug)

            obj = form.save(commit=False)
            obj.save()
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ArticleAndCommentView, self).get_context_data(**kwargs)
        context["article"] = Article.objects.get(slug=self.kwargs["slug"])
        return context
