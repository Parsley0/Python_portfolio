from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name ...',
            'id': 'name',
            'name': 'name',
            'class': 'form-control',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@gmail.com',
            'id': 'email',
            'name': 'email',
            'class': 'form-control',
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your Message ...',
            'rows': 5,
            'id': 'message',
            'name': 'message',
            'class': 'form-control',
        }),
    )
