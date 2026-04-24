from django.http import HttpResponse, HttpRequest

from .models import Product, products

def index(request:HttpRequest):
    return HttpResponse('<h1 style="color: darkgreen;">Start work with Django</h1>')

def get_person(request:HttpRequest, name, surname):
    return HttpResponse(f'<h1>Name: {name} Surname: {surname}')

def get_product(request:HttpRequest, id:int=-1):
    if id > len(products) or id < 0:
        return HttpResponse('<h1 style="color: darkred;">Product not found</h1>')
    return HttpResponse(str(products[id]))

def get_request(request:HttpRequest):
    request_info = f"""
    <ul>
    <li> Host: {request.get_host()}</li>
    <li> Port: {request.get_port()}</li>
    <li> Path: {request.path}</li>
    <li> Path info: {request.path_info}</li>
    <li> GET: </li>
        <ul>
    """
    
    for key, value in request.GET.items():
        request_info += f"<li> {key}: {value}</li>"
    
    request_info += "</ul></ul>"
    return HttpResponse(request_info)
