# Generated by Django 3.1.5 on 2021-01-27 11:44

from django.db import migrations
import django_jalali.db.models
import loan.models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_auto_20210126_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='bring',
            field=django_jalali.db.models.jDateTimeField(validators=[loan.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='carry',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]
