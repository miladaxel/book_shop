from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author, Category

class BookList(ListView):
    model = Book
    template_name = 'home/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

class BookDetail(DetailView):
    model = Book
    template_name = 'home/book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class CategoryList(ListView):
    model = Category
    template_name = 'home/category_list.html'
    context_object_name = 'categories'

#برای لیست یک کتگوری خاص
class CategoryBooksView(DetailView):
    model = Category
    template_name = 'home/category_book.html'
    context_object_name = 'category'
    slug_field = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_categories'] = self.object.book_categories.all()
        return context



class AuthorDetailView(DetailView):
    model = Author
    template_name = 'home/author_detail.html'
    context_object_name = 'author'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'