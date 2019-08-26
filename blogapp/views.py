from django.shortcuts import render , redirect , get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.

def index(request):
    Blogs = Blog.objects.all().order_by('-id')
    return render(request , 'index.html' ,{'Blogs' : Blogs})


def post(request): 
    if request.method == 'POST': #등록
        forms = BlogForm(request.POST)  
        if forms.is_valid():
            forms.save()
            return redirect('index')       
    else: #수정
        forms = BlogForm()
    return render(request , 'post.html' ,{'forms' : forms})

def detail(request , blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    
    
    return render(request , 'detail.html', {'detail':details})