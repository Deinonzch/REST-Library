from django.contrib.auth.models import User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Book(models.Model):
    TYPE = (('book', 'book'), ('comics', 'comics'), ('manga', 'manga'), ('e-book', 'e-book'))
    GENRE = (('SCI-FI', 'SCI-FI'), ('horror', 'horror'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPE)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRE)
    describe = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=17)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code book.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Book, self).save(*args, **kwargs)


class LendBook(models.Model):
    idU = models.ForeignKey(User, related_name='lend_book', on_delete=models.CASCADE)
    idB = models.ForeignKey(Book, related_name='lend_book', on_delete=models.CASCADE)
    date_lend = models.DateField()
    date_end_lend = models.DateField()
    give_up = models.BooleanField(default=False)
    highlighted = models.TextField()

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.date_lend > self.date_end_lend:
            raise ValidationError('Start date cannot precede end date')
    '''
    def save(self, *args, **kwargs):
        # you can have regular model instance saves use this as well
        super(LendBook, self).save(*args, **kwargs)
'''
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(LendBook, self).save(*args, **kwargs)