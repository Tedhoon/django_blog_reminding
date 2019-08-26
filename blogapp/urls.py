from django.urls import path ,include
from .views import *

urlpatterns = [
    
    path('blog/', index , name = 'index'),
    path('post/', post , name= 'post'),
    path('blog/<int:blog_id>/' , detail, name='detail'),
]