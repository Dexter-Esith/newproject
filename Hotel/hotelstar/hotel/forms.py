from django import forms
from .models import Test, HotelReview

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'gender')

class HotelReviewForm(forms.ModelForm):
    class Meta:
        model = HotelReview
        fields = ('name', 'email', 'comment', 'rating_number')