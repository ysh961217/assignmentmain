from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def write(request):
    blogs = Blog.objects
    return render(request, 'blog/write.html', {'blogs': blogs})