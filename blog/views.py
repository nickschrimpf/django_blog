from django.shortcuts import render

# Create your views here.
blog_posts = {
    '0':'post about learning Django',
    '1':'post about making a blog',
    '2':'post about Gardening',
    '3':'post about design',
    '4':'post about tacos',
}

def index(request):
    return render(request,"blog/index.html")

def posts(request):
    return render(request,"blog/index.html")