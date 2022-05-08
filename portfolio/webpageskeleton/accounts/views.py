from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods


# Create your views here.

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:home')
    
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():

            signed_user = signup_form.save()
            auth_login(request, signed_user)
            return redirect('community:home')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:home')

    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'community:home')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)    

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:home')

@require_safe
def profile(request, username):
    if request.user.is_authenticated:
        target = get_object_or_404(get_user_model(),username=username)
        context = {
            'target': target,
        }
        return render(request, 'accounts/profile.html', context)
    return redirect('accounts:login')

@require_http_methods(['GET', 'POST'])
def user_update(request, username):
    target = get_object_or_404(get_user_model(),username=username)
    if request.method == 'POST':
        user_update_form = CustomUserChangeForm(request.POST, instance = target)
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect(request.GET.get('next') or 'community:home')
    else:
        user_update_form = CustomUserChangeForm(instance = target)
    context = {
        'target': target,
        'user_update_form': user_update_form,
    }
    return render(request, 'accounts/update.html', context)


@require_POST
def user_delete(request, username):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('community:home')    

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request, username):
    target = get_object_or_404(get_user_model(),username=username)
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request, password_change_form.user)
            return redirect('community:home')
    else:
        password_change_form = PasswordChangeForm(request.user)
    context = {
        'target': target,
        'password_change_form': password_change_form,
    }
    return render(request, 'accounts/change_password.html', context)

@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        target = get_object_or_404(get_user_model(), username=username)
        user = request.user
        if target != user:
            if target.followers.filter(pk=user.pk).exists():
                target.followers.remove(user)
            else:
                target.followers.add(user)
    return redirect('accounts:profile', target.username)