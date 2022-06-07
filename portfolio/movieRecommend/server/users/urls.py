from django.urls import path
from . import views
urlpatterns = [
    path('profile/<username>/',views.user_profile),
    path('profile/<username>/follow/',views.user_follow),

]