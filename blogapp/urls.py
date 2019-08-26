from django.urls import path
from .views import *
urlpatterns = [
    path('blog/', views.index , 'index'),
    path('blog/<int:pk>' , views.detail, 'detail'),
]