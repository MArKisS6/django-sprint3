from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

MAX_POST = 5

def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:MAX_POST]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    ).order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'post_list': post_list
        }
    )
