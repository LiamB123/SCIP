from django.urls import path
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path(r'^$', get_posts, name='get_posts'),
    path(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    path(r'^new/$', create_or_edit_post, name='new_post'),
    path(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
    ]