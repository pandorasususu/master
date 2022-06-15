from django.urls import path
from . import views

urlpatterns = [
    path('',views.read_or_create_articles),
    path('<int:article_pk>/', views.detail_or_update_or_delete_article),
    path('<int:article_pk>/like/', views.like_article),
    path('<int:article_pk>/comment/', views.create_comment),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.update_or_delete_comment),
    path('<int:article_pk>/comment/<int:comment_pk>/like', views.like_comment),
]