from django.urls import path
from . import views
urlpatterns = [
    path('profile/<username>/',views.user_profile_or_follow),
    path('<int:movie_id>/',views.read_or_create_rating),
    path('<int:movie_id>/<int:rating_pk>/',views.update_or_delete_rating),
    path('<int:movie_id>/<int:rating_pk>/like',views.like_rating),
]