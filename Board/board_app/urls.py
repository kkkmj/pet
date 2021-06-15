from django.urls import path
from . import views

appname='bootstrap_study'
urlpatterns = [
    path('', views.index, name='index'),
]
