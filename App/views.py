from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from App.models import Article, Comment

# Create your views here.

def home(request):
    return render(request, 'App/home.html', {})

@login_required
def bulletin_board_list(request):
    """掲示板一覧ページ"""
    if request.method == 'POST':
        article = Article(title=request.POST['title'], text=request.POST['text'], posted_at=timezone.now())
        article.save()
    
    else:
        articles = Article.objects.order_by('-posted_at')

    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'App/bulletin_board_list.html', context)

@login_required
def bulletin_board(request, article_id):
    """掲示板ページ"""
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        comment = Comment(article=article, text=request.POST['text'], posted_at=timezone.now())
        comment.save()

    context = {
        'article':  article,
        'comments': article.comments.order_by('-posted_at')
    }
    return render(request, 'App/bulletin_board.html', context)

