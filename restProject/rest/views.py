from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest.models import Book, LendBook
from rest_framework import viewsets
from rest.serializers import UserSerializer, BookSerializer, LendBookSerializer
from rest_framework import generics
from rest.permissions import *
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'lend_books': reverse('lend_book-list', request=request, format=format),
    })

class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        genre = self.kwargs['genre']
        return Book.objects.filter(genre=genre)

class AuthorBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        author = self.kwargs['author']
        return Book.objects.filter(author=author)

class TypeBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        type = self.kwargs['type']
        return Book.objects.filter(type=type)

class TypeAndGenreBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        type = self.kwargs['type']
        genre = self.kwargs['genre']
        return Book.objects.filter(type=type, genre=genre)

class AuthorAndGenreBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        author = self.kwargs['author']
        genre = self.kwargs['genre']

        return Book.objects.filter(author=author, genre=genre)

class IsbnAndGenreBookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        isbn = self.kwargs['isbn']
        genre = self.kwargs['genre']

        return Book.objects.filter(isbn=isbn, genre=genre)

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LendBookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = LendBook.objects.all()
    serializer_class = LendBookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsIdUOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)