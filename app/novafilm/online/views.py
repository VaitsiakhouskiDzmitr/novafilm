from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Post

def hello(request):

    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'online/post_list.html', context={'page':page, 'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request,'online/post_detail.html', context={'post': post})
