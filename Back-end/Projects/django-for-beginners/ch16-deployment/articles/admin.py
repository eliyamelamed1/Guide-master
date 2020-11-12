from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin) # display apps and its database's model Post on the admin page
admin.site.register(Comment)
