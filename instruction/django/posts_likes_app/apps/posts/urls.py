from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^create/(?P<post_id>\d+)$', views.create_like),
    url(r'^destroy/(?P<post_id>\d+)$', views.destroy_like),
]