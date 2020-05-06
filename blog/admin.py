from django.contrib import admin

from .models import Main, Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Main)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
