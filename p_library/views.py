from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from p_library.models import Book, Redaction


def book_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    numbers = [i for i in range(1, 101)]
    data_library = {
        "title": "Welcome to my person library!",
        "books": books,
        "numbers": numbers,
    }
    return HttpResponse(template.render(data_library, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    data_redact = {
        "redactions": redactions,
    }
    return HttpResponse(template.render(data_redact, request))