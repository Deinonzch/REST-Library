from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views
from rest.views import BookViewSet, LendBookViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
'''
urlpatterns = [
    url(r'^book_list/$', views.book_list),
    url(r'^book_list/(?P<pk>[0-9]+)/$', views.book_operation),
    url(r'^user_list/$', views.user_list),
    url(r'^user_list/(?P<pk>[0-9]+)/$', views.user_operation),
    url(r'^lend_book_list/$', views.lend_book_list),
    url(r'^lend_book_list/(?P<pk>[0-9]+)/$', views.lend_book_list)
]
'''
'''
lend_book_list = LendBookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
lend_book_detail = LendBookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
lend_book_highlight = LendBookViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
book_list = BookViewSet.as_view({
    'get': 'list'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^book_list/$', book_list, name='book-list'),
    url(r'^book_list/(?P<pk>[0-9]+)/$', book_detail, name='book-detail'),
    url(r'^user_list/$', user_list, name='user-list'),
    url(r'^user_list/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^lend_book_list/$', lend_book_list, name='lend_book-list'),
    url(r'^lend_book_list/(?P<pk>[0-9]+)/$', lend_book_detail, name='lend_book-detail'),
    url(r'^lend_books/(?P<pk>[0-9]+)/highlight/$', lend_book_highlight, name='lend_book-highlight'),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
'''

schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'lend_books', views.LendBookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]