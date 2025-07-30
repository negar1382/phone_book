from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<str:department>', views.index, name='index'),
]