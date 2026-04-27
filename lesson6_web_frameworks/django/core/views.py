from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse
from http import HTTPStatus
from .models import Product, products
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer


def json_response(request:HttpRequest):
    return JsonResponse({
        "status_code": 404,
        "reason_phrase": "not-found",
        "data": None
    })


def get_products_json(request:HttpRequest):
    return JsonResponse(products, ProductSerializer, safe=False)

def index(request:HttpRequest):
    return HttpResponse('<h1 style="color: darkgreen;">Start work with Django</h1>')

def get_person(request:HttpRequest, name, surname):
    return HttpResponse(f'<h1>Name: {name} Surname: {surname}')

def get_product(request:HttpRequest, id:int=-1):
    r = HttpResponse()
    if id > len(products) or id < 0:
        r.status_code = HTTPStatus.NOT_FOUND
        r.content = '<h1 style="color: darkred;">Product not found</h1>'
        
        return r
        # return HttpResponseNotFound('<h1 style="color: darkred;">Product not found</h1>')
        #return HttpResponse('<h1 style="color: darkred;">Product not found</h1>')
    return HttpResponse(str(products[id]))

items = []

@csrf_exempt
def post_view(request:HttpRequest):
    content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post">
        <input type="text" name="taskName" placeholder="Enter task">
        <button type="submit">Add</button>
    </form>
    <ol>
    '''
    if request.method == 'POST':
        item = request.POST.get("taskName", None)
        if item is not None: items.append(item)
        
    for item in items:
        content += f"<li>{item}</li>"
    
    content+='''
    </ol>
</body>
</html>
    '''
    return HttpResponse(content)

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
