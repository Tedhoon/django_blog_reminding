from django.shortcuts import render , redirect , get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.

def index(request):
    Blogs = Blog.objects.all().order_by('-id')
    return render(request , 'index.html' ,{'Blogs' : Blogs})


def post(request): 
    if request.method == 'POST': #글쓰기 등록
        forms = BlogForm(request.POST)  
        if forms.is_valid():
            forms.save()
            return redirect('index')       
    else: #글쓰기 페이지 들어가기
        forms = BlogForm()
    return render(request , 'post.html' ,{'forms' : forms})

def detail(request , blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    
    
    return render(request , 'detail.html', {'detail':details})


def edit(request, detail_id):
    #먼저 해당 객체폼을 가져와야하잖아!
    detail = get_object_or_404(Blog, pk = detail_id)
    #여기서 진짜 중요 edit에 detail.id를 넘기고 싶으니까 객체 이름을 이렇게 똑같이 해줘야합니다 ㅠㅠ
    # 그러니까 정리하자면 pk값을 쓰기 위해 get_object_or_404로 가져와야서 넘겨줘야함

    editblogform = BlogForm(instance = detail)
    if request.method == 'POST':
        editblogforms = BlogForm(request.POST , instance = detail) #흐름대로 설명하자면 해당 블로그 pk값 블록폼을 instance로 가져오고 requset.POST내용을 저장한다 이말임
        if editblogforms.is_valid():
            editblogforms.save()
            return redirect('index')
    
    return render(request, 'edit.html' ,{'editblogform':editblogform , 'detail' : detail})


def delete(request , blog_id):
    detail = get_object_or_404(Blog, pk = blog_id)
    detail.delete()
    return redirect('index')