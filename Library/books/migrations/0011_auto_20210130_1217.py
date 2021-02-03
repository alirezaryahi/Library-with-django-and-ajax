# Generated by Django 3.1.5 on 2021-01-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20210130_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='_author_books_+', to='books.Book'),
        ),
    ]