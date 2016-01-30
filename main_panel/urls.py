from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.main_index, name='main_index'),
url(r'^logout/$', views.logout, name='logout'),
url(r'^editName/$', views.changeName, name='editName'),
]
