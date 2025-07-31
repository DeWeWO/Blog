from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def blog_entries(request):
    return render(request, 'core/blog.html')

def post_details(request):
    return render(request, 'core/post-details.html')

def contact(request):
    return render(request, 'core/contact.html')