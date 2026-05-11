from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="startPage"),
    path('postuser/', views.postuser, name="userPost"),
]
