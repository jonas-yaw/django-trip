from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model


class Article(models.Model):
    def author_default():
        return CustomUser.objects.get(username="Jonas").username

    def slug_default():
        return " "

    title = models.CharField(max_length=144)
    description = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default=author_default, max_length=144)

    slug = models.SlugField(max_length=255, blank=True, default=slug_default)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.article.slug})
