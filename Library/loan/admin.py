from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Borrow


# Register your models here.


class BorrowAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'book', 'carry', 'bring', 'remainingTime']
    search_fields = ['user']

    class Meta:
        model = Borrow


admin.site.register(Borrow, BorrowAdmin)
