from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post
from datetime import date
from django.contrib.auth.forms import User
from accounts.models import UserProfile

def blog_list(request):
    articles = Post.objects.all().order_by('date')
    if request.method == 'POST':
        add = forms.CreateArticle(request.POST,request.FILES)
        if add.is_valid():
            instance = add.save(commit=False)
            instance.author = request.user
            instance.save()
            # return redirect('blog:bloglist')
    else:
        add = forms.CreateArticle()
    return render(request,'blog/listview.html',{'articles':articles,'add': add})

@login_required(login_url="accounts:login")
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('article_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked =True
    return redirect('blog:bloglist')
