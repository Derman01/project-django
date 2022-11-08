from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rubric/<int:id>', views.rubric, name='rubric'),
    path('show/<int:id>', views.show, name='show')
    path('hashtag/<int:id>', view.hash_tag, name='hashtag')
]