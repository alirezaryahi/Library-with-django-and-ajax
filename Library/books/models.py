from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author/', null=True, blank=True)
    about = models.TextField(default='')
    books = models.ManyToManyField(Book, related_name='+', blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)
    books = models.ManyToManyField(Book, related_name='+', blank=True)

    def __str__(self):
        return self.title
