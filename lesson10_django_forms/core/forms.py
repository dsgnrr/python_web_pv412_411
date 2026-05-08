from django import forms
from django.forms import widgets

choices=[
    (1, "Item1"),
    (2, "Item2"),
    (3, "Item3"),
]

class UserForm(forms.Form):
    name_field = forms.CharField(label="Name", initial="Tom", widget=widgets.TextInput(
        attrs={"class":"validate"}))
    name_field2 = forms.CharField(label="Name2", widget=widgets.TextInput(
        attrs={"class":"validate"}))
    surname_field = forms.CharField(label="Surname", widget=widgets.TextInput(
        attrs={"class":"validate"}
    ))

class TestForm(forms.Form):
    # BooleanField -> input:checkbox
    # EmailField -> input:email
    # IntegerField/DecimalField/FloatField -> input:number
    
    field_order = ["password","name_field", "surname_field"]
    
    # Output: <input type="text">
    name_field = forms.CharField(label="Name", initial="Tom", help_text="Enter name", widget=widgets.TextInput(
        attrs={"name": 'name_field'}))
    name_field2 = forms.CharField(label="Name2", widget=widgets.TextInput(
        attrs={"name": 'name_field'}))
    surname_field = forms.CharField(label="Surname")
    
    password = forms.CharField(widget=widgets.PasswordInput, label='Password')
    
    about = forms.CharField(widget=widgets.Textarea(attrs={"class":"materialize-textarea"}))
    
    hidden = forms.CharField(widget=widgets.HiddenInput)
    
    # set_item = forms.ChoiceField(choices=choices)
    set_items = forms.MultipleChoiceField(choices=choices)
    
    
    
    