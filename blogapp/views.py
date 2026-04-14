from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, UserRegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else: #Normal user
            posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})
@login_required
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    return render(request, 'blogapp/create_post.html', {'form': PostForm()})

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})