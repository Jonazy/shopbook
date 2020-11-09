from django.shortcuts import render, get_object_or_404
from .models import Category, Book
from cart.carts import Cart
from cart.forms import CartAddBookForm
# Create your views here.


def home(request, category_slug=None):
    category = None
    book_total_per_cat = None
    categories = Category.objects.all()
    books = Book.objects.filter(in_stock=True)
    book_total = books.count()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(category=category, in_stock=True)
        book_total_per_cat = books.count()
    context = {
        'books': books,
        'categories': categories,
        'category': category,
        'book_total': book_total,
        'book_total_per_cat': book_total_per_cat,
    }
    return render(request, 'book/index.html', context)


def detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    cart_form = CartAddBookForm()
    context = {
        'book': book,
        'cart_form': cart_form,
    }
    return render(request, 'book/detail.html', context)