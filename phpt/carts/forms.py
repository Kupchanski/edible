from django import forms
from .models import Carts


class NewCartForm(forms.ModelForm):
    class Meta:
        model = Carts
        fields = [
            'category',
            'title',
            'developer',
            'img',
            'place',
            'comment',
        ]


class UpdateCartForm(forms.ModelForm):
    class Meta:
        model = Carts
        fields = [
            'category',
            'cart_color',
            'title',
            'developer',
            'img',
            'place',
            'comment',
        ]