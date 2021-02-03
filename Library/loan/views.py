from datetime import timedelta
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from books.models import Book
from .forms import OrderForm
from django.utils import timezone
from .models import Borrow
from django.contrib.auth.decorators import login_required
import jdatetime
from datetime import datetime

now = datetime.now()


# Create your views here.

@login_required(login_url='/user-admin-login')
def order(request, *args, **kwargs):
    book_id = kwargs['id']
    book = Book.objects.get(id=book_id)
    user = User.objects.get(username=request.user.username)
    # -----------------limit of book order---------------------
    borrow_item = []
    borrow = Borrow.objects.all()
    for br in borrow:
        if br.user_id == user.id:
            borrow_item.append(br.book_id)
    # -----------------------------------------------------------
    error = ''
    form = OrderForm(request.POST or None,
                     initial={'book': book.title, 'user': request.user.username,
                              'carry': jdatetime.date.fromgregorian(day=now.day, month=now.month,
                                                                    year=now.year)})
    if request.method == 'POST':
        if form.is_valid():
            bring = form.cleaned_data.get('bring')
            carry = form.cleaned_data.get('carry')
            if bring < timezone.now().date():
                error = 'تاریخ انتخاب شده باید بیشتر از تاریخ کنونی باشد'
            elif bring > timezone.now().date() + timedelta(7):
                error = 'کتاب بیشتر از 7 روز به امانت داده نمی شود'
            elif len(borrow_item) >= 2 and book.title != form.cleaned_data.get('book'):
                error = 'بیشتر از 2 کتاب نمی توانید امانت بگیرید'
            else:
                if len(borrow_item):
                    if book.id in borrow_item:
                        br = Borrow.objects.get(book=book.id)
                        br.bring = bring
                        br.remainingTime = bring - jdatetime.date.fromgregorian(day=now.day, month=now.month,
                                                                                year=now.year)
                        br.save()
                        return redirect('/order-status')
                    else:
                        Borrow.objects.create(book=book, user_id=user.id, carry=carry, bring=bring,
                                              remainingTime=bring - jdatetime.date.fromgregorian(day=now.day,
                                                                                                 month=now.month,
                                                                                                 year=now.year))
                        book.available = False
                        book.save()
                        return redirect('/')
                else:
                    Borrow.objects.create(book=book, user_id=user.id, carry=carry, bring=bring,
                                          remainingTime=bring - jdatetime.date.fromgregorian(day=now.day,
                                                                                             month=now.month,
                                                                                             year=now.year))
                    book.available = False
                    book.save()
                    return redirect('/')

    context = {'form': form, 'error': error}
    return render(request, 'order-status.html', context)


@login_required(login_url='/user-admin-login')
def order_status(request):
    borrow = Borrow.objects.all()
    order_list = []
    for item in borrow:
        if item.user_id == request.user.id:
            order_list.append(item)
    context = {'items': order_list}
    return render(request, 'status-ordering.html', context)
