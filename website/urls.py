from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("library/", views.LibraryView.as_view(), name="library"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("book_detail/<int:id>/", views.book_details , name="book_detail"),
    path("book_detail/<int:pk>/delete/", views.DeleteBook.as_view(), name="delete"),
    path("book_detail/<int:pk>/edit/", views.EditBook.as_view(), name="edit"),
    path("add_book/", views.CreateBook.as_view(), name="add_book"),
]