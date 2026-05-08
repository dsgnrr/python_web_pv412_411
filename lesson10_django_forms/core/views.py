from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from . import forms

def index(request:HttpRequest):
    # if request.method == 'POST':
    #     print("POST:", request.POST)
    #     return redirect('registerPage')
        
    if request.method == 'GET':
        # верстка
        # return render(request, "form_page.html") 
        
        # клас форми
        return render(request, 'django_form.html', {"form":forms.UserForm()})
    else:
        resp = HttpResponse(content="Method not allowed")
        resp.status_code = 405
        return resp

def postuser(request:HttpRequest):
    if request.method == 'POST':
        print("POST:", request.POST)
        name = request.POST.getlist('name_field', None)
        surname = request.POST.get('surname_field', None)
        
        if len(name) <= 0 or len(surname) <=0:
            return render(request, 'user_page.html', {"error_message": "All fields required"})
        
        return render(request, "user_page.html",{
            "name": name[0],
            "surname": surname
        })
        
        # return redirect('registerPage')
    else:
        resp = HttpResponse(content="Method not allowed")
        resp.status_code = 405
        return resp