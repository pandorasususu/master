from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/',views.profile,name='profile'),
    path('<str:username>/update/',views.user_update,name='user_update'),
    path('<str:username>/password/', views.change_password, name='change_password'),
    path('<str:username>/delete/',views.user_delete,name='user_delete'),
    path('<str:username>/follow/',views.follow,name='follow'),

]