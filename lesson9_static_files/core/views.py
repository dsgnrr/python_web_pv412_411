from django.shortcuts import render
from .models import Contact, contacts

def index(request):
    return render(request, 'main_page.html')

def contactsPage(request):
    print(contacts)
    return render(request,'contacts.html', {'contacts': contacts})
