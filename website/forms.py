from django import forms
from .models import Book, Comment

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "pages", "published_date", "cover", "author" )


class BookEditForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')

