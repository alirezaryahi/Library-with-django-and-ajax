from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from books.models import Book
from django_jalali.db import models as jmodels


# from .views import validate_date


# Create your models here.

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='', verbose_name='عنوان کتاب')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام کاربری')
    carry = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ امانت بردن')
    bring = jmodels.jDateField(validators=[validate_date], verbose_name='تاریخ انقضا')
    remainingTime = models.CharField(default='', max_length=100)

    def __str__(self):
        return f'${self.book}'
