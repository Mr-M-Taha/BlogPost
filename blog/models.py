from typing import override

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @override
    def __str__(self):
        return f" post id: {self.id} / post title: {self.title}"

    def get_absolute_url(self):
        return reverse("blog:post-details", kwargs={"pk": self.pk})
