from django import forms
from .models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["email", "name", "phone", "message"]
        
        widgets = {
            "email":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"example@gmail.com"}),
            "name":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"Anna Myradow"}),
            "phone":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"+99361234567"}),
            "message":forms.Textarea(attrs={'class':"required sm-form-control", 'placeholder':". . ."}),
        }