from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Book, Comment
from .forms import AddBook,BookEditForms, CommentForm

@login_required
def index(request, *args, **kwargs):
    if request.method == "GET": 
        latest_added_books = Book.objects.all()[:5]
        context = {
            "latest_added_books": latest_added_books,
        }
        return render(request, 'index.html', context=context)


class AboutView(TemplateView):
    template_name = "about.html"
    context_object_name = "about"


class LibraryView(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "library.html"
    context_object_name = "book_libs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_authors'] = Author.objects.all()
        context['number_of_books'] = Book.objects.all().count()
        context['number_of_authors'] = Book.objects.all().count()
        context['number_of_books_sold'] = Book.objects.filter(status__exact="Sold").count()
        context['number_of_books_rented'] = Book.objects.filter(status__exact='Rented').count()
        context['number_of_books_available'] = Book.objects.filter(status__exact='Available').count()
        return context


def book_details(request, id):
    book_detail = get_object_or_404(Book, id=id)
    comments =  book_detail.comments_book.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book_detail = book_detail
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'book_detail': book_detail,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment
    }

    return render(request, 'book_detail.html', context=context)




class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBook
    template_name = "add_book.html"
    context_object_name = "add_book" 
    success_url = reverse_lazy("library")

    def form_valid(self, form): # new
        form.instance.user = self.request.user
        return super().form_valid(form)



class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "delete_book.html"
    context_object_name = "delete"
    success_url = reverse_lazy("library")


class EditBook(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'edit_book.html'
    context_object_name = "edit"
    fields = "__all__"
    success_url = reverse_lazy("library")

