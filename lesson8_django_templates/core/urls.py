from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='startPage'),
    path('text-format/', views.text_format, name='textFormat')
]
