from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    keywords = models.CharField(max_length=200, verbose_name='Ключевые слова')
    annotation = models.TextField(verbose_name='Аннотация')
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение', default='images/empty.jpg')
    rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE, null=True)

    def first_sentence(self):
        return self.annotation.split('.')[0]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class Rubric(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', db_index=True)

    def get_absolute_url(self):
        return reverse('index', kwargs={'rubric_id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрику'
        verbose_name_plural = 'Рубрики'


class Hashtag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'