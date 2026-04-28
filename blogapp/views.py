from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
def home(request):
    # Show all posts on the home page for every user
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('home')
    return render(request, 'blogapp/create_post.html', {'form': PostForm()})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blogapp/my_posts.html', {'posts': posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return HttpResponseForbidden("You don't have permission to delete this post.")
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('my_posts')
    # If not POST, redirect back
    return redirect('post_details', post_id=post.id)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return HttpResponseForbidden("You don't have permission to edit this post.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('post_details', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogapp/edit_post.html', {'form': form, 'post': post})
