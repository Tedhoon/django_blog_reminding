from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    Blogs = Blog.objects.all()
    return render(request , 'index.html' ,{'Blogs' : Blogs})


def detail(request , blog_id):
    return render(request , 'detail.html')