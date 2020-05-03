from django.contrib import admin

from .models import Main, Category, Post, Comment

admin.site.register(Main)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

