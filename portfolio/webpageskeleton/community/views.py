from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

@require_safe
def home(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'community/home.html', context)

@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    comment_form = CommentForm()
    if request.user.is_authenticated:
        context = {
            'article': article,
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'community/detail.html', context)
    return redirect('community:home')

@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article_create_form = ArticleForm(request.POST)
            if article_create_form.is_valid():
                article = article_create_form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('community:article_detail', article.pk)
        else:
            article_create_form = ArticleForm()
        context = {
            'article_create_form': article_create_form,
        }
        return render(request, 'community/create.html', context)
    return redirect('accounts:login')


@require_http_methods(['GET','POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user == article.user:
                article_form = ArticleForm(request.POST, instance=article)
                if article_form.is_valid():
                    article = article_form.save(commit=False)
                    article.save()
                #     return redirect('community:detail', article.pk)
                # return redirect('community:detail', article.pk)
            return redirect('community:detail', article.pk)

        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article': article,
            'article_form': article_form,
        }
        return render(request, 'community/update.html', context)
    return redirect('accounts:login')


@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('community:home')
        return redirect('community:detail', article.pk)
    return redirect('accounts:login')

@require_POST
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticate:
        if request.user != article.user:
            if article.like_users.filter(pk=request.user).exists():
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
            # return redirect('community:detail', article.pk)
        return redirect('community:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('community:article_detail', article.pk)
        context = {
            'article': article,
            'comments': article.comments,
            'comment_form': CommentForm(),
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')

@require_http_methods(['GET','POST'])
def comment_update(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST, instance=comment)
        if request.user == comment.user:
            if comment_form.is_valid():
                comment_form.save()
                return redirect('community:detail', article_pk)
        context = {
            'article': article,
            'comments': article.comments,
            'comment_form': CommentForm(insance=comment),
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('community:article_detail', article_pk)

@require_POST
def comment_like(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated:
        if request.user != comment.user:
            if comment.like_users.filter(pk=request.user.pk).exists():
                comment.like_users.remove(request.user)
            else:
                comment.like_users.add(request.user)
        return redirect('community:detail', article_pk)
    return redirect('accounts:login')
