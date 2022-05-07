## SOCIAL LOGIN

참고 링크: https://django-allauth.readthedocs.io/en/latest/installation.html



1) **python package 설치**

```
pip install django-allauth
```



2. **settings.py 필요 요소 확인**

​	#1. TEMPLATES

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # 아래의 구문 들어가 있는지 확인
                'django.template.context_processors.request',
            ],
        },
    },
]
```

​	

​	#2.AUTHENTICATION_BACKENDS

```python
AUTHENTICATION_BACKENDS = [
    ...
    # 아래 구문 추가
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]
```



​	#3.INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    # 아래 요소 없으면 추가:
    
    #Native
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',
	
    #3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # 필요에 따라 추가, 예시에는 GOOGLE을 통한 로그인 서비스 구현을 위해 GOOGLE 추가
    'allauth.socialaccount.providers.google',
]
```



​	#4. SITE ID

INSTALLED_APPS의 django.contrib.sites는 하나의 django 서버에서 여러개의 url, site들을 관리할 때 사용

[The “sites” framework](https://docs.djangoproject.com/en/4.0/ref/contrib/sites/#module-django.contrib.sites)

Use it if your single Django installation powers more than one site and you need to differentiate between those sites in some way.



django.contrib.sites를 사용하기 위해서는 SITE_ID 설정이 필요

[SITE_ID](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SITE_ID)
The ID, as an integer, of the current site in the django_site database table. This is used so that application data can hook into specific sites and a single database can manage content for multiple sites.

```python
SITE_ID = 1
```



3. urls.py 추가

```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```





4. **GCP 접속**

#1. 프로젝트 생성

#2. 탐색 메뉴 -> API 및 서비스 

#3.  OAuth 동의 화면

#3.1 User Type 외부 클릭하고 만들기

#3.2. 필요 정보 입력

#3.3. 범위 단계에서 수집할 유저 정보 범위 선택

#3.4. 테스트 사용자 설정 -> 완료

#4. 좌측 메뉴의 '사용자 인증 정보'로 이동 

#4.1 상단의 '+ 사용자 인증 정보 만들기' -> OAuth 클라이언트 ID

#4.2 승인된 리디렉션 URI

https://django-allauth.readthedocs.io/en/latest/providers.html

상단의 링크에서 사용하고자 하는 로그인 서비스 찾아서 해당 링크 기입

(구글의 경우 http://127.0.0.1:8000/accounts/google/login/callback/)

#5. 위 과정 완료 후 클라이언트ID, 클라이언트 보안 비밀번호 저장



5. **admin 접속**

#1. python manage.py migrate

#2. python manage.py runserver

#3. admin 페이지 접속

#4. 소셜계정 -> 소셜 어플리케이션 -> 소셜 어플리케이션 추가

#5. 클라이언트 아이디, 비밀 키에 3번 과정 마지막에서 얻은 정보 입력

#6. sites에 실제 사용할 도메인 입력



6. **templates 작성**

https://django-allauth.readthedocs.io/en/latest/templates.html

소셜 로그인 기능을 수행코자 하는 html 페이지에 아래의 작업 수행

```html
{% load socialaccount %}

<a href="{% provider_login_url "google"%}">Google</a>
```

