import textwrap
from django.db import models
from django.contrib.auth import get_user_model

from core.models import PublishedModel

User = get_user_model()

MAX_LEN = 256
MAX_POST = 5
MAX_STR = 50

class Location(PublishedModel):
    name = models.CharField(
        max_length=MAXL,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return textwrap.shorten(
            self.title, 
            width=MAX_STR, 
            placeholder='...'
        )




class Category(PublishedModel):
    title = models.CharField(
        max_length=MAXL,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены символы латиницы, '
            'цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return textwrap.shorten(
            self.title, 
            width=MAX_STR, 
            placeholder='...'
        )


class Post(PublishedModel):
    title = models.CharField(
        max_length=MAXL,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — можно делать '
            'отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return textwrap.shorten(
            self.title, 
            width=MAX_STR, 
            placeholder='...'
        )
