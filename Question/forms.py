from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            'firstname': forms.TextInput(attrs={'class': "col-md-6 col-sm-12", 'placeholder': "Firstname"}),
            'lastname': forms.TextInput(attrs={'class': "col-md-6 col-sm-12", 'placeholder': "Lastname"}),
            'email': forms.EmailInput(attrs={'class': "col-md-6 col-sm-12", 'placeholder': "Email"}),
            'subject': forms.TextInput(attrs={'class': "col-md-12 col-sm-12", 'placeholder': "Subject"}),
            'message': forms.Textarea(attrs={'class': "col-lg-12", 'placeholder': "Message"})
        }

