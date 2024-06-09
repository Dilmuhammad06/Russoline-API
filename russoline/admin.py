from django.contrib import admin
from .models import Content, Comment, Follow, Like

admin.site.register([Content, Comment, Follow, Like])
