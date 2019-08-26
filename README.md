# 그냥 심심해서 복습겸 백지코딩

+= 디테일페이지에서 CRUD구현하기
<h3>컨닝 리스트</h3>

<li>디펄트 주소 커스텀함

```python
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda r : redirect('index') , name = "root"), #최상위 주소로 갈 때 redirect시키기

    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
```
<li>누적이 안되게 하려면 blogform(instance = pk값)하고 form.save()해줘야함
<li>pk값을 쓰기 위해 get_object_or_404로 가져와야서 직접... 손수 .....넘겨줘야함!
<li>수정을 위해 해당 블로그 폼을 불러오려면 instance를 쓰면 된다 

```python
editblogform = BlogForm(instance = detail) 
```