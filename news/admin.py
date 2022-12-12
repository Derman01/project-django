from django.contrib import admin
from .models import Article, Rubric, Hashtag, Image


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'annotation', 'image', 'rubric')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Hashtag)
admin.site.register(Image)
