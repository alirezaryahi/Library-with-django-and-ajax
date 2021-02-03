# Generated by Django 3.1.5 on 2021-01-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210130_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='authors',
            field=models.ManyToManyField(blank=True, to='books.Author'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='_subject_books_+', to='books.Book'),
        ),
    ]