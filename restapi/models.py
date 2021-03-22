from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(('first name'), max_length=150)
    last_name = models.CharField(('last name'), max_length=150)
    email = models.EmailField(('email addres'), max_length=60, unique=True)
    image = models.ImageField(('photo'), blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        """
        Return the username of user
        """
        return self.get_username()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('User', related_name='author', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
