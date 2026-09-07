from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(
        request,
        'blog/category.html',
        {
            'category_slug': category_slug
        }
    )
