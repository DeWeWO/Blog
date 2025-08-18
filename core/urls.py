from django.urls import path
from .views import index, about, blog_entries, post_details, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog_entries, name='blog_entries'),
    path('post/<slug:post_slug>/', post_details, name='post_details'),
    path('contact/', contact, name='contact'),
]