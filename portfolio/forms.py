from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'name@example.com',
                'class': 'input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+91 9xxxxxxxxx',
                'class': 'input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project or query...',
                'class': 'textarea',
                'rows': 6
            }),
        }
