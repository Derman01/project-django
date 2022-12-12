from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rubric/<int:id>', views.rubric, name='rubric'),
    path('article/<int:id>', views.show_article, name='article'),
    path('hashtag/<int:id>', views.hash_tag, name='hashtag'),
    path('rubric/add', views.add_rubric, name='rubric_add'),
    path('hashtag/add', views.add_hashtag, name='hashtag_add'),
    path('article/add', views.add_article, name='article_add')
]