from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
