from django.shortcuts import render, get_object_or_404
from .models import Post


def lista_post(request):
    posts = Post.published.all()
    return render(request, 'blog/post/lista.html', {'posts': posts})


def detalles_post(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, estado='publico', publicado__year=year, publicado__month=month, publicado__day=day)
    return render(request, 'blog/post/detalles.html', {'post': post})