from django.shortcuts import render
from django.http import HttpRequest

import random

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def __str__(self):
        return f"""
    <div style="border: 1px solid">
        <p>Name: {self.name}</p>
        <p>Surname: {self.surname}</p>
        <p>Age: {self.age}</p>
    <div>
    """


def index(request: HttpRequest):
    context = {}
    context['welcome_text'] = "Hello, Dear user, have a nice day"
    context['html_tag'] = '<h3 style="color: darkred;"> HTML tag </h3>'
    context['script_tag'] = '''
    <script>
        alert("Autoescape off");
    </script>
    '''
    
    context['int_value'] = 10
    context['float_value'] = 10.5312
    context['bool_value'] = False
    
    context['list'] = ["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    context['dict']= {"key1": "value1"}
    context['object']= Person('William', 'Butcher', 45)
    context['random'] = random.randint(-2,11)
    
    return render(request, "index.html", context=context)
