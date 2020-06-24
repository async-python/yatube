from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Возвращает до 11 последних записей."""
    latest = list(Post.objects.all().select_related(
        'author', 'group'
    ).values(
        'author', 'group', 'pub_date', 'text', 'author__first_name',
        'author__last_name'
    )[:11])
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    """Возвращает до 12 записей группы или ошибку, если группы нет."""
    group = get_object_or_404(Group, slug=slug)
    posts = list(group.posts.all().select_related(
        'author', 'group'
    ).values(
        'author', 'group', 'pub_date', 'text', 'author__first_name',
        'author__last_name'
    )[:12])
    return render(request, "group.html", {"group": group, "posts": posts})


