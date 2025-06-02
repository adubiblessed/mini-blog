from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, BlogForm, CommentForm, LoginForm
from .models import Blog, User, Comment
from django.utils.text import Truncator

# Create your views here.
def home(request):
    user = User.objects.get(id=request.session.get('user_id')) if request.session.get('user_id') else None
    blogs = Blog.objects.all().select_related('author').order_by('-created_at')
    return render(request, 'blogapp/home.html', {'user':user,'blogs': blogs})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'blogapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'blogapp/login.html', {'form': form})

def post_detail(request, slug, username):
    user = get_object_or_404(User, username=username)
    blog = get_object_or_404(Blog, slug=slug, author__username=username)  # safer than .get()
    comments = blog.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.author = User.objects.get(id=request.session['user_id'])
            comment.save()
            return redirect('post_detail', username=user.username, slug=slug)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blogapp/post_details.html', {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
        'user': user,
    })

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = User.objects.get(id=request.session['user_id'])
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blogapp/create_blog.html', {'form': form})
def profile(request, username):
    user = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(author=user).order_by('-created_at')
    return render(request, 'blogapp/profile.html', {'user': user, 'blogs': blogs})

def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('profile', username=user.username)
    else:
        form = UserForm(instance=user)
    return render(request, 'blogapp/edit_profile.html', {'form': form, 'user': user})

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def edit_blog(request, slug, username):
    user = get_object_or_404(User, username=username)
    blog = get_object_or_404(Blog, slug=slug, author__username=username)
    user_id = request.session.get('user_id')
    is_author = True
    if blog.author.id != request.session.get('user_id'):
        is_author = False
        return redirect('home')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=slug, username=username)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/edit_blog.html', {'form': form, 'blog': blog, 'user': user, 'is_author': is_author,})

def delete_blog(request, slug, username):
    user = get_object_or_404(User, username=username)
    blog = get_object_or_404(Blog, slug=slug, author__username=username)
    if blog.author.id != request.session.get('user_id'):
        return redirect('home') 
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blogapp/delete_blog.html', {'blog': blog})