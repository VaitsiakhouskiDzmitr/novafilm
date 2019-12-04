
from django.shortcuts import render, get_object_or_404

from .models import Post



def hello(request, tag_slug=None):

    posts = Post.objects.all()


    return render(request, 'online/post_list.html', context={'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)


    return render(request, 'online/post_detail.html', context={'post': post,})
