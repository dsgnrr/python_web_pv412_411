from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseNotAllowed
from .forms import UserForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from datetime import datetime


form = UserForm()

def index(req: HttpRequest):
    return render(req, "django-form.html", {"form": form})



def postuser(req:HttpRequest):
    if req.method == 'POST':
        # print("POST: ", req.POST)
        # return redirect("startPage")
        
        userform = UserForm(req.POST, req.FILES)
        if userform.is_valid():
            
            name = userform.cleaned_data["name"]
            surname = userform.cleaned_data["surname"]
            age = userform.cleaned_data["age"]
            
            picture = userform.cleaned_data["picture"]
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_type = picture.name.split('.')[-1]
            file_name = fs.save(f"{datetime.timestamp(datetime.now())}.{file_type}", picture)
            return render(req, "user_page.html", {
                "name": name,
                "surname": surname,
                "age": age,
                "imageUrl": fs.url(file_name)
            })
        global form
        form = userform
        return redirect("startPage")
    else: return HttpResponseNotAllowed(["POST",])