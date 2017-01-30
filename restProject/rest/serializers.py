from django.contrib.auth.models import User
from rest.models import LendBook, Book
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lend_books = serializers.HyperlinkedRelatedField(many=True, view_name='lend_book-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')


class LendBookSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='lend_book-highlight', format='html')
    class Meta:
        model = LendBook
        fields = ('idU', 'idB', 'date_lend', 'date_end_lend', 'give_up')

        idU = serializers.ReadOnlyField(source='idU.id')

        def validate(self, data):
            """
            Check that the start is before the stop.
            """
            if data['date_lend'] > data['date_end_lend']:
                raise serializers.ValidationError("finish must occur after start")
            return data


class BookSerializer(serializers.HyperlinkedModelSerializer):
    lend_books = serializers.HyperlinkedRelatedField(many=True, view_name='lend_book-detail', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'type', 'author', 'genre', 'describe', 'isbn')
