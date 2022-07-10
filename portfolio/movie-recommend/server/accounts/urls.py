from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profile/<username>/delete/', views.delete, name='delete'),
    path('profile/<username>/follow/', views.follow, name='follow'),
]
