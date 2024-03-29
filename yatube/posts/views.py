from django.shortcuts import render, get_object_or_404

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


# View-функция для страницы сообщества:
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = 'Записи сообщества'
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
