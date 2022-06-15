"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/community/', include('community.urls')),
    path('api/v1/users/', include('users.urls')),

    # movie 앱 폴더를 따로 만들지 않은 이유는 영화와 관련된 상세정보는 TMDB API를 통해 불러오고,
    # 이 프로젝트의 DB에서 저장하고 있는 정보는 유저의 별점/평가와 관련된 정보이기 때문
    path('api/v1/movies/', include('users.urls')),
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
    # path('api/v1/accounts/google/', views.GoogleLogin),

]
