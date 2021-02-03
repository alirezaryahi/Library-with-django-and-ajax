from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from loan.models import Borrow
from .models import Book, Subject, Author
from django.utils import timezone
from django.views import generic
import json
from .forms import BookForm


# Create your views here.

# def home(request):
#     borrows = Borrow.objects.all()
#     items = []
#     # --------Erasing a trust that is out of date-----------------
#     time = []
#     for borrow in borrows:
#         items.append(borrow)
#         time.append(borrow.bring)
#     for item in time:
#         if item < timezone.now():
#             borrow = Borrow.objects.get(bring=item)
#             borrow.delete()
#     # -----------------------------------------------------------
#     books = Book.objects.all()
#     for book in books:
#         book.available = True
#         book.save()
#     if len(items):
#         for item in items:
#             for book in books:
#                 if book.id == item.book_id:
#                     book.available = False
#                     book.save()
#     else:
#         for book in books:
#             book.available = True
#             book.save()
#     context = {'books': books}
#     return render(request, 'main.html', context)


class HomeView(generic.ListView):
    model = Book
    template_name = 'main.html'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        borrows = Borrow.objects.all()
        books = Book.objects.all()
        items = []
        # --------Erasing a trust that is out of date-----------------
        time = []
        for borrow in borrows:
            items.append(borrow)
            time.append(borrow.bring)
        for item in time:
            if item < timezone.now():
                borrow = Borrow.objects.get(bring=item)
                book = Book.objects.get(id=borrow.book_id)
                book.available = True
                book.save()
                borrow.delete()
        # -----------------------------------------------------------
        if len(items):
            for item in items:
                for book in books:
                    if book.id == item.book_id:
                        book.available = False
                        book.save()
        return data


def book(request, *args, **kwargs):
    title = kwargs['title'].replace('-', ' ')
    books = Book.objects.filter(subject__title=title)
    context = {'books': books}
    return render(request, 'main.html', context)


def author(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors.html', context)


def author_detail(request, *args, **kwargs):
    name = kwargs['name'].replace('-', ' ')
    author = Author.objects.get(name=name)
    context = {'author': author}
    return render(request, 'author-detail.html', context)


def search(request):
    qs = request.GET.get('q')
    context = {}
    if qs is not None and qs.strip() != '':
        context['books'] = Book.objects.filter(Q(title__icontains=qs) | Q(subject__title__icontains=qs))
        context['authors'] = Author.objects.filter(name__icontains=qs)
    return render(request, 'main.html', context)


def autocomplete(request):
    if request.is_ajax():
        qs = request.GET.get('query', '')
        books = Book.objects.filter(Q(title__icontains=qs))
        results = []
        for book in books:
            book_json = {}
            book_json['title'] = book.title
            results.append(book_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def book_update(request):
    if request.is_ajax():
        book_id = request.GET.get('query', '')
        print(book_id)
        book = Book.objects.get(id=book_id)
        subjectt = Subject.objects.get(id=book.subject_id)
        authorr = Author.objects.get(id=book.author_id)
        subjects = Subject.objects.all()
        subject_list = []
        for subject in subjects:
            subject_list.append(subject.title)
        authors = Author.objects.all()
        author_list = []
        for author in authors:
            author_list.append(author.name)
        data = {'id': book.id, 'title': book.title, 'subject': subjectt.title, 'author': authorr.name,
                'available': book.available, 'subjects': subject_list, 'authors': author_list}
        data = json.dumps(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def book_update_done(request):
    if request.is_ajax():
        id = request.POST.get('id', '')
        title = request.POST.get('title', '')
        subject = request.POST.get('subject', '')
        author = request.POST.get('author', '')
        available = request.POST.get('available', '')
        if request.POST.get('available', '') == 'true':
            available = True
        else:
            available = False
        subjectClass = Subject.objects.get(title=subject)
        authorClass = Author.objects.get(name=author)
        book = Book.objects.get(id=id)
        # --------------Remove book and author from subject and author before edit ----------
        subjects = Subject.objects.all()
        authors = Author.objects.all()
        for subjectt in subjects:
            subjectt.books.remove(book)
            subjectt.save()
        for authorr in authors:
            authorr.books.remove(book)
            authorr.save()
        #--------------------------------------------------------------------------------
        subjectClass.books.add(book)  # add book to subject
        authorClass.books.add(book)  # add book to author
        book.title = title
        book.subject_id = subjectClass.id
        book.author_id = authorClass.id
        book.available = available
        book.save()
        subject_instance = Subject.objects.get(id=book.subject_id)
        author_instance = Author.objects.get(id=book.author_id)
        data = {'title': book.title, 'subject': subject_instance.title, 'author': author_instance.name,
                'available': book.available}
        data = json.dumps(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def book_delete(request):
    if request.is_ajax():
        book_id = request.GET.get('query', '')
        data = {'id': book_id}
        data = json.dumps(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def book_delete_done(request):
    if request.is_ajax():
        book_id = request.POST.get('id', '')
        book = Book.objects.get(id=book_id)
        book.delete()
        data = {'done': 'done'}
        data = json.dumps(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def add_book(request):
    form = BookForm(request.POST or None)
    error = ''
    if form.is_valid():
        title = form.cleaned_data.get('title')
        subject = form.cleaned_data.get('subject')
        author = form.cleaned_data.get('author')
        if subject == None or author == None:
            error = 'تمام موارد باید پر شود'
        else:
            Book.objects.create(title=title, subject=subject, author=author)
            book = Book.objects.get(title=title)
            author = Author.objects.get(name=author)
            subject = Subject.objects.get(title=subject)
            author.books.add(book.id)
            subject.books.add(book.id)
            author.save()
            subject.save()
            return redirect('/')
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add-book.html', context)
