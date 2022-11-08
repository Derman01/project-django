from django.shortcuts import render, get_object_or_404
from .models import Article, Rubric


def get_base_context():
    rubrics = Rubric.objects.all();
    return {'rubrics': rubrics}


def create_context(new_context):
    context = get_base_context()
    context.update(new_context)
    return context


def index(request):
    news = Article.objects.all()
    return render(request, 'news/index.html', create_context({'news': news}))


def rubric(request, id):
    news = Article.objects.filter(rubric_id=id)
    return render(request, 'news/index.html', create_context({'news': news, 'rubric_id': id}))


def show(request, id):
    new = get_object_or_404(Article, pk=id)
    rubric_name = Rubric.objects.get(id=new.rubric_id)
    return render(request, 'news/show.html', create_context({'new': new, 'rubric_name': rubric_name}))

def hash_tag(request, id):