from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Article(models.Model):
    def author_default():
        return CustomUser.objects.get(username="Jonas").username

    def slug_default():
        return " "

    title = models.CharField(max_length=144)
    description = models.TextField()
    image = models.ImageField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default=author_default, max_length=144)

    slug = models.SlugField(max_length=255, blank=True ,default=slug_default)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
