# from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(publicationType='NI').order_by('-publicationDate')


class PostDetail(DetailView):
    model = Post
    template_name = 'ni.html'
    context_object_name = 'ni'
    queryset = Post.objects.filter(publicationType='NI')