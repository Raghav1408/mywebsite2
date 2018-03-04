from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    # for a album /music/album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # for a album /music/album_id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]