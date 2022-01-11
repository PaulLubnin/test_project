from rest_framework.viewsets import ModelViewSet

from books_core.models import Book
from books_core.serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
