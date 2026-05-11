from django import forms
from django.forms import widgets

class UserForm(forms.Form):
    
    error_css_class = "error-text"
    
    name = forms.CharField(max_length=100, required=True, label="First Name", 
                           widget=widgets.TextInput(attrs={
                               "placeholder": "First Name",
                               "class": "validate"
                           }))
    surname = forms.CharField(max_length=100, required=True, label="Second Name",
                              widget=widgets.TextInput(attrs={
                                  "class":"validate"
                              }))
    age = forms.IntegerField(min_value=18, required=True, label="Age",
                              widget=widgets.NumberInput(attrs={
                                  "class":"validate"
                              }))
    picture = forms.ImageField(required=False)
    
    # clean_<field_name>
    
    # Валідація для конкретного поля, пілся clean_ підставляйте назву свого поля
    def clean_name(self):
        data = self.cleaned_data["name"]
        
        if "joe" in str(data).lower():
            self.add_error("name", "Contains 'joe'")
            return data
        return data
    
    # Валідація всієї форми
    def clean(self):
        result = super().clean()
        surname = result["surname"]
        if "due" in str(surname).lower():
            self.add_error("surname", "Contains 'due'")
            return result
        return result