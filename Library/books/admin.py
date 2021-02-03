from django.contrib import admin
from .models import Book, Author, Subject


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'author', 'available']
    search_fields = ['title', 'author', 'subject']
    list_filter = ('available',)

    class Meta:
        model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = Author


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Subject


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Subject, SubjectAdmin)
