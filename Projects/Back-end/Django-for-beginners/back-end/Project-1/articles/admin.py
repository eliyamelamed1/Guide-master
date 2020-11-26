from django.contrib import admin
from .models import Article, Comment


# this 2 functions Display all the comments of a single Article on the admin  

# Determine in which way the comments will be designed on the admin 
# Tabular = comments have lower height
# Stacked = comments have laragr height
class CommentInline(admin.TabularInline): # new
    model = Comment
    # extra = 0 # by defailt django will display 3 empty rows, this is the way to change it.

# Display all of the Article's comments, beneath the article on the admin page.
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin) # display apps and its database's model Post on the admin page
admin.site.register(Comment)
