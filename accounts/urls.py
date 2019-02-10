from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('update/', views.edit_user, name="updateprofile"),


]
