from django.contrib.auth.models import User
from rest.models import LendBook, Book
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')


class LendBookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LendBook
        fields = ('user', 'book', 'date_lend', 'date_end_lend', 'give_up')

        user = serializers.ReadOnlyField(source='user')
        book = serializers.ReadOnlyField(source='book')

        def validate(self, data):
            """
            Check that the start is before the stop.
            """
            if data['date_lend'] > data['date_end_lend']:
                raise serializers.ValidationError("finish must occur after start")
            return data


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'type', 'author', 'genre', 'describe', 'isbn')
