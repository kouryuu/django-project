from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.index, name='index'),
url(r'^log/$', views.log, name='log'),
url(r'^create/$', views.create, name='create'),


]
