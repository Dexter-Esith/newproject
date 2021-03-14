from django import forms
from .models import Test, HotelReview, Contact

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'gender')

class HotelReviewForm(forms.ModelForm):
    class Meta:
        model = HotelReview
        fields = ('name', 'email', 'comment', 'rating_number')
        # exclude ანუ რასაც შიგნით შევიტანტ იმის გარდა გამოიტანოს ყველაფერი.
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'comment': forms.Textarea(attrs={'class': 'form-control'}),
        #     'rating_number': forms.Select(attrs={'class': 'form-control'})
        # }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')