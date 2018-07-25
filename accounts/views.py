from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, UserProfileForm
from blog.forms import CreateArticle
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            # if'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            return redirect('blog:bloglist')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:bloglist')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("blog:bloglist")

def profile_view(request):
    if request.method == 'POST':
        add = CreateArticle(request.POST,request.FILES)
        if add.is_valid():
            instance = add.save(commit=False)
            instance.author = request.user
            instance.save()
            # return redirect('blog:bloglist')
    else:
        add = CreateArticle()
    user = request.user
    return render(request, 'accounts/profile.html', {'form':user,'add': add})


@login_required
def edit_user(request):
    id= request.user.id
    user = User.objects.get(id=id)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('bio','country','website','phone','city','photo'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return redirect('accounts:profile')

        return render(request, "accounts/update.html", {
            "noodle": id,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
