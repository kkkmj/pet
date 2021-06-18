from django.urls import path
from . import views

appname='bootstrap_study'
urlpatterns = [
    path('', views.index, name='index'),
    path('list_com1', views.list_com1, name='list_com1'),
    path('list_com2', views.list_com2, name='list_com2'),
    path('list_com3', views.list_com3, name='list_com3'),
    path('post_com1', views.post_com1, name='post_com1'),
    path('post_com2', views.post_com2, name='post_com2'),
    path('post_com3', views.post_com3, name='post_com3'),
    path('post_com1/<int:id>', views.detail1, name='detail1'),
    path('post_com2/<int:id>', views.detail2, name='detail2'),
    path('post_com3/<int:id>', views.detail3, name='detail3'),
    path('post_com1/comment_write', views.comment_write, name='comment_write'),
    path('post_com1/post_detail', views.post_detail, name='post_detail'),
]
