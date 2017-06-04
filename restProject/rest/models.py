from django.contrib.auth.models import User
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Book(models.Model):
    TYPE = (('book', 'book'), ('comics', 'comics'), ('manga', 'manga'), ('e-book', 'e-book'))
    GENRE = (('Sci-Fi', 'Sci-Fi'), ('Horror', 'Horror'), ('Shounen', 'Shounen'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPE)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRE)
    describe = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=17)


class LendBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_lend = models.DateField()
    date_end_lend = models.DateField()
    give_up = models.BooleanField(default=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.date_lend > self.date_end_lend:
            raise ValidationError('Start date cannot precede end date')
    '''
    def save(self, *args, **kwargs):
        # you can have regular model instance saves use this as well
        super(LendBook, self).save(*args, **kwargs)
'''