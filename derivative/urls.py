from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^derive/$', views.getDerivative, name='getDerivative'),
]
