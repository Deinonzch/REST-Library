from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views
from rest.views import *
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(title='Pastebin API')
swagger_view2 = get_swagger_view(title='Pastebin API')
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'lend/books', views.LendBookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('^schema/$', schema_view),
    url('^$', swagger_view2),
    url(r'^', include(router.urls)),
    #url('^books/author/(?P<author>.+)/$', AuthorBookViewSet.as_view()),
    #url('^books/type/(?P<type>.+)/$', TypeBookViewSet.as_view()),
    #url('^books/genre/(?P<genre>.+)/$', GenreBookViewSet.as_view()),
    url('^books/genre/(?P<genre>.+)/author/(?P<author>.+)/$', AuthorAndGenreBookViewSet.as_view()),
    url('^books/genre/(?P<genre>.+)/type/(?P<type>.+)/$', TypeAndGenreBookViewSet.as_view()),
    url('^books/genre/(?P<genre>.+)/isbn/(?P<isbn>.+)/$', IsbnAndGenreBookViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]