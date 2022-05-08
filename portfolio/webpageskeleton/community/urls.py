from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:article_pk>/',views.article_detail,name='article_detail'),

    path('create/',views.article_create,name='article_create'),
    path('<int:article_pk>/delete',views.article_delete,name='article_delete'),
    path('<int:article_pk>/update/',views.article_update,name='article_update'),
    path('<int:article_pk>/like',views.article_like,name='article_like'),

    path('<int:article_pk>/create/',views.comment_create,name='comment_create'),
    path('<int:article_pk>/<int:comment_pk>/delete',views.comment_delete,name='comment_delete'),
    path('<int:article_pk>/<int:comment_pk>/update',views.comment_update,name='comment_update'),
    path('<int:article_pk>/<int:comment_pk>/like',views.comment_like,name='comment_like'),



]