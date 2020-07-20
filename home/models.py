from django.db import models
from django.urls import reverse


class Suggest(models.Model):
    suggestion = models.TextField()

    def __str__(self):
        return self.suggestion

    def get_absolute_url(self):
        return reverse("suggest_done")

