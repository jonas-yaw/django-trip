from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField()
    image = models.ImageField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        CustomUser.objects.get(username="Jonas"), on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse("articledetail", kwargs={"slug": self.slug})
