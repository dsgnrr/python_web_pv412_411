from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='registerPage'),
    path('user/', views.postuser, name='postUser')
]
