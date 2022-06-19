from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('random/', views.movie_list_random_get),
    path('list/', views.movie_list_get),
    path('recommend/<username>/', views.movie_recommend),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/save/', views.movie_save),
    path('<int:movie_id>/rating/<username>/', views.movie_rating),
    path('toprated/', views.movie_toprated),
    path('popular/', views.movie_popular),
    path('recent/', views.movie_recent),
]