from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UserEdit
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import jdatetime


# Create your views here.


def user_admin_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm(request.POST or None)
        if request.method == 'POST':
            if 'user' in request.POST:
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=username, password=password)
                    if user is not None and not user.is_superuser:
                        login(request, user)
                        return redirect('/')
                    else:
                        form.add_error('username', 'کاربری با این مشخصات یافت نشد')
            if 'admin' in request.POST:
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=username, password=password)
                    if user is not None and user.is_superuser:
                        login(request, user)
                        return redirect('/')
                    else:
                        form.add_error('username', 'کاربری با این مشخصات یافت نشد')

        context = {'form': form}
        return render(request, 'login.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        User.objects.create_user(username=username, email=email, password=password, is_active=True)
        return redirect('/user-admin-login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/user-admin-login')
def change_profile(request):
    user_id = request.user.id
    user_detail = User.objects.get(id=user_id)
    context = {}
    form = UserEdit(request.POST or None,
                    initial={'first_name': user_detail.first_name, 'last_name': user_detail.last_name,
                             'email': user_detail.email})
    context['form'] = form

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user_detail.first_name = first_name
        user_detail.last_name = last_name
        user_detail.email = email
        user_detail.save()

    return render(request, 'change-profile.html', context)


def user_list(request):
    users = User.objects.all()
    for user in users:
        user.date_joined = jdatetime.date.fromgregorian(day=user.date_joined.day, month=user.date_joined.month,
                                                        year=user.date_joined.year)
        user.last_login = jdatetime.date.fromgregorian(day=user.last_login.day, month=user.last_login.month,
                                                       year=user.last_login.year)
    context = {'users': users}
    return render(request, 'user-list.html', context)


def active_deactive(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        if user.is_active:
            user.is_active = 0
        else:
            user.is_active = 1
        user.save()
    return redirect('user-list')
