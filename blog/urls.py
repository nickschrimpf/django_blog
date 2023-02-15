from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="welcome-page"),
    path('posts',views.posts_page,name="posts-page"),
    path('posts/<slug:slug>',views.post_detail,name="post-detail-page")
]
