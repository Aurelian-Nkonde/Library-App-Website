from django.contrib import admin
from .models import Author, Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "pages", "published_date")
    list_filter = ["title", "published_date"]
    raw_id_fields = ('author',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "nationality")
    list_filter = ["first_name"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
