from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostImage
from .forms import PostForm
import requests
from environs import Env

env = Env()
env.read_env()

def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            images = form.cleaned_data.get("images")
            for image in images:
                PostImage.objects.create(post=post, image=image)
            return redirect("blog_entries")
    return render(request, "core/create_post.html", {"form": form})

def blog_entries(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {"posts": posts})

def post_details(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'core/post-details.html', {"post": post})

def post_update(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)  # get() o'rniga get_object_or_404()
    images = PostImage.objects.filter(post=post)
    
    if request.method == "POST":
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save()
            
            new_images = form.cleaned_data.get("images")
            if new_images:
                for image in new_images:
                    PostImage.objects.create(post=post, image=image)
            
            deleted_images = request.POST.getlist('deleted_images')
            if deleted_images:
                PostImage.objects.filter(id__in=deleted_images).delete()
                
            return redirect("blog_entries")
    else:
        form = PostForm(instance=post)
    
    return render(request, 'core/update-post.html', {
        'form': form, 
        'images': images,
        'post': post
    })

def post_delete(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    post.delete()
    return redirect("blog_entries")

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    BOT_TOKEN = env.str('BOT_TOKEN')
    GROUP_CHAT_ID = env.str('GROUP_CHAT_ID')
    URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        text = f"<b>Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: </b> <i>{message}</i>"
        response = requests.post(url=URL, data={
            "chat_id": GROUP_CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        })
        print(response)
    return render(request, 'core/contact.html')