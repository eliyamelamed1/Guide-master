from django.contrib import admin
from .models import Book, Review

# adding the Review model and specifying a display of inline
class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",) # update file to specify which fields to display.

admin.site.register(Book, BookAdmin)
