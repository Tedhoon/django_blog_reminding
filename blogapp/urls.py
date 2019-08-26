from django.urls import path ,include
from .views import *

urlpatterns = [
    path('blog/', index , name = 'index'),
    path('blog/<int:pk>' , detail, name='detail'),
]