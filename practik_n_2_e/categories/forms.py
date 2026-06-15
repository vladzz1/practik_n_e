from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label='Назва категорії',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Назва категорії ...'
        })
    )

    description = forms.CharField(
        label='Опис',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Короткий опис ...'
        })
    )

    slug = forms.SlugField(
        label='Slug',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'category-name'
        })
    )

    image = forms.ImageField(
        label='Зображення',
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Category
        fields = ('name', 'description', 'slug', 'image')