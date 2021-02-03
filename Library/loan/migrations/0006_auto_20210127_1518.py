# Generated by Django 3.1.5 on 2021-01-27 11:48

from django.db import migrations
import django_jalali.db.models
import loan.models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_auto_20210127_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='bring',
            field=django_jalali.db.models.jDateField(validators=[loan.models.validate_date], verbose_name='تاریخ انقضا'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='carry',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ امانت بردن'),
        ),
    ]