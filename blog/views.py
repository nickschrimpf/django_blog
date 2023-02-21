from django.shortcuts import render, get_object_or_404

from .models import Post



def index(request):
    sorted_posts = Post.objects.order_by("-date")
    latest_posts = sorted_posts[:2]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts_page(request):
    all_posts = Post.objects.all()
    return render(request,"blog/posts.html",{
        "posts":all_posts
    })

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,"blog/post-detail.html",{
        "post":post,
        "tags":post.tags.all()
    })