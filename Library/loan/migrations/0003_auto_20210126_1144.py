# Generated by Django 3.1.5 on 2021-01-26 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_available'),
        ('loan', '0002_auto_20210125_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='book',
        ),
        migrations.AddField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
