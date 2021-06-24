from django.shortcuts import render, get_object_or_404
from .models import Shop
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def post_list(request):
    object_list = Shop.objects.filter(status='published')
    paginator = Paginator(object_list, 2) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
        'shop/post/list.html',
        {'page': page,
        'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Shop, slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(request,
        'shop/post/detail.html',
        {'post': post})