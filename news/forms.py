from django import forms
from .models import Rubric as RubricModel, Hashtag as HashtagModel, Article, Image


class Rubric(forms.Form):
    name = forms.CharField(max_length=100, label='Название', required=True)


class Hashtag(forms.Form):
    name = forms.CharField(max_length=100, label='Название', required=True)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'keywords', 'annotation', 'rubric', 'image')
        label = {
            'title': 'Заголовок',
            'keywords': 'Ключевые слова',
            'rubric': 'Рубрика',
            'image': 'Изображение'
        }


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')