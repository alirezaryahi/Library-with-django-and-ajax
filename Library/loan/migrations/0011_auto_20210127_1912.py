# Generated by Django 3.1.5 on 2021-01-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_auto_20210127_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='remainingTime',
            field=models.CharField(default='', max_length=100),
        ),
    ]