from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'نام کابری ...', 'class': 'form-control vazir direction'}))
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور ...', 'class': 'form-control vazir direction'}))


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'نام کابری ...', 'class': 'form-control vazir direction'}))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل ...', 'class': 'form-control vazir direction'}))
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور ...', 'class': 'form-control vazir direction'}))
    re_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار رمز عبور ...', 'class': 'form-control vazir direction'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_user_exist = User.objects.filter(username=username).exists()
        if is_user_exist:
            raise forms.ValidationError('نام کاربری تکراری است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_email_exist = User.objects.filter(email=email).exists()
        if is_email_exist:
            raise forms.ValidationError('ایمیل تکراری است')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('پسورد نباید کمتر از 8 کاراکتر باشد')
        return password

    def clean_re_password(self):
        re_password = self.cleaned_data.get('re_password')
        password = self.cleaned_data.get('password')
        if password != re_password:
            raise forms.ValidationError('رمز های عبور با هم مطابقت ندارد')
        return re_password


class UserEdit(forms.Form):
    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'نام ...', 'class': 'form-control vazir direction'}))
    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی ...', 'class': 'form-control vazir direction'}))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل ...', 'class': 'form-control vazir direction'}))

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError('نام کاربری نباید کمتر از 3 کاراکتر باشد')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError('نام کاربری نباید کمتر از 3 کاراکتر باشد')
        return last_name
