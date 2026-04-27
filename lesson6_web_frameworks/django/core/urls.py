from django.urls import path

from . import views

"""
    <str:prop_name> - path("person/<str:name>")
    <int:prop>
    <slug:prop> samsung-ultra-s24, tom-due-12
    <path:prop> example/
    <uuid:prop> 0a9c7753-957e-5fa4-8a7f-b79ea515486e
"""



urlpatterns = [
    path('', views.index, name='homePage'),
    path('person/', views.get_person, kwargs={"name":'Tom', 'surname':'Due'} ,name='personPage'),
    path('product/<int:id>', views.get_product, name='productById'),
    path('request/', views.get_request, name='requestInfo'),
    path('post/', views.post_view, name='postView'),
    path('json/', views.json_response, name="jsonView"),
    path('products-json/', views.get_products_json, name="jsonProducts")
]
