# Generated by Django 4.0 on 2022-01-27 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_core', '0002_bookinstance_borrower_alter_book_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
