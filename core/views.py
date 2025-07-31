from django.shortcuts import render
import requests
from environs import Env

env = Env()
env.read_env()


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def blog_entries(request):
    return render(request, 'core/blog.html')

def post_details(request):
    return render(request, 'core/post-details.html')

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