from django.shortcuts import render, redirect
from .models import Post
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
            product = form.save()
            print(product)
            return redirect("blog_entries")
    return render(request, "core/create_post.html", {"form": form})

def blog_entries(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {"posts": posts})

def post_details(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'core/post-details.html', {"post": post})

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