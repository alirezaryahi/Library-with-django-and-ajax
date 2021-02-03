from django import forms
from functools import partial
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import Borrow

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class OrderForm(forms.Form):
    book = forms.CharField(label='', disabled=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control vazir direction'}))
    user = forms.CharField(label='', disabled=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control vazir direction'}))
    carry = forms.CharField(label='', disabled=True,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control vazir direction'}))
    bring = JalaliDateField(widget=AdminJalaliDateWidget())

    class Meta:
        model = Borrow
        fields = ('book', 'user', 'carry', 'bring')
