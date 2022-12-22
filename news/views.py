from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Rubric, Hashtag
from .forms import Rubric as Rubric_form, Hashtag as Hashtag_form, ArticleForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def superuser_required(function):

    @login_required
    def function_return(request):
        if request.user.is_superuser:
            return function(request)
        else:
            return redirect('index')
    return function_return


def index(request):
    news = Article.objects.all()
    return render(request, 'news/index.html', {'news': news})


def rubric(request, id):
    news = Article.objects.filter(rubric_id=id)
    return render(request, 'news/index.html', {'news': news, 'rubric_id': id})


def show_article(request, id):
    new = get_object_or_404(Article, pk=id)
    return render(request, 'news/article.html', {'new': new})


def hash_tag(request, id):
    articles = get_object_or_404(Hashtag, pk=id).articles.all()
    print(articles[0])
    return render(request, 'news/index.html', {'news': articles})


@superuser_required
def add_rubric(request):
    if request.method == 'POST':
        form = Rubric_form(request.POST)
        if form.is_valid():
            try:
                Rubric.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления Рубрики')
    else:
        form = Rubric_form()
    return render(request, 'news/form/rubric.html', {'form': form})

@superuser_required
def add_hashtag(request):
    if request.method == 'POST':
        form = Hashtag_form(request.POST)
        if form.is_valid():
            try:
                Hashtag.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, 'Ошибка добавления Хэштега')
    else:
        form = Hashtag_form()
        return render(request, 'news/form/hashtag.html', {'form': form})

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form.add_error(None, 'Ошибка добавления статьи')
            return render(request, 'news/form/article.html', {'form': form})
    else:
        form = ArticleForm()
        return render(request, 'news/form/article.html', {'form': form})