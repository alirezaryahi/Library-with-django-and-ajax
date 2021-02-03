from django import forms
from pip._vendor.webencodings import labels

from books.models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(label='عنوان کتاب ', widget=forms.TextInput(
        attrs={'placeholder': 'نام کتاب را وارد کنید ...', 'class': 'form-control vazir mb-4 direction'}))

    class Meta:
        model = Book
        fields = ('title', 'subject', 'author', 'available')
        labels = {
            'subject': 'موضوع ',
            'author': 'نویسنده ',
            'available': 'موجود / ناموجود '
        }
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control vazir direction mt-2 mb-4'}),
            'author': forms.Select(attrs={'class': 'form-control vazir direction mt-2 mb-4'}),
        }
