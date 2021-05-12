from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=200)

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('author-detail',  args[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.ImageField(upload_to="imgs", default="default.jpg")
    CATEGORIES = (
    ('T', 'Thriller'),
    ('R', 'Romantic'),
    ('D', 'Documentary'),
    ('L', 'Literature')
    )

    category_field = models.CharField(max_length=50, choices=CATEGORIES, default="Unknown")

    AVAILABILITY = (
        ('Sold', 'Sold'),
        ('Available', 'Available'),
        ('Rented', 'Rented')
    )

    status = models.CharField(max_length=10, choices=AVAILABILITY)

    class Meta:
        ordering = ['-title']
    
    def get_absolute_url(self):
        return reverse('book-detail', args[str(self.id)])

    def __str__(self):
        return self.title



class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments_book")
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name