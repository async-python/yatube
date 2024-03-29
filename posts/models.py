from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='содержание')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='дата публикации'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts",
        verbose_name='автор'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="posts", verbose_name='группа'
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text
