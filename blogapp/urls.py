from django.urls import path

from .views import (
    home,
    profile,
    create_blog,
    edit_blog,
    delete_blog,
    register,
    login_view,
    logout_view,
    post_detail,
    edit_profile,
)

urlpatterns = [
    path('', home, name='home'),
    path('profile/<username>/', profile, name='profile'),
    #path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('create/', create_blog, name='create_blog'),
    path('edit/<str:username>/<slug:slug>/', edit_blog, name='edit_blog'),
    path('delete/<str:username>/<slug:slug>/', delete_blog, name='delete_blog'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post/<str:username>/<slug:slug>/', post_detail, name='post_detail'),
    path('edit_profile/<str:username>/', edit_profile, name='edit_profile'),
]