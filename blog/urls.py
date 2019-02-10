from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views

app_name='blog'

urlpatterns = [
    path('', views.blog_list, name="bloglist"),
    path('like/', views.like_post, name="likepost"),
]
