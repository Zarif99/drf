from django.contrib import admin
from django.contrib.auth.models import Group

from restapi.models import Article, User

admin.site.register(User)
admin.site.register(Article)
admin.site.unregister(Group)