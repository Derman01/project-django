from django import template
from news.models import Rubric, Hashtag

register = template.Library()


@register.inclusion_tag('news/header.html')
def show_rubrics(rubric_id):
    rubrics = Rubric.objects.all()
    return {'rubrics': rubrics, 'rubric_id': rubric_id}