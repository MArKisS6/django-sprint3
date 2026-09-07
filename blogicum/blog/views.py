# from django.shortcuts import render
# from django.http import Http404


# posts_id = {post['id']: post for post in posts}


# def index(request):
#    return render(request, 'blog/index.html', {'posts': posts})


# def post_detail(request, post_id):
#    post = posts_id.get(post_id)
#    if post is None:
#       raise Http404('Запись блога с таким ID не найдена.')
#    return render(request, 'blog/detail.html', {'post': post})


# def category_posts(request, category_slug):
# return render(
# request,
# 'blog/category.html',
# {
#     'category_slug': category_slug,
# }
#    )
