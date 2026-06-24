from django import forms
from .models import Product
from categories.models import Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Назва категорії',
        widget=forms.Select(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'Назва категорії ...',
        })
    )

    name = forms.CharField(
        label='Назва продукту',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'Назва продукту ...',
        })
    )

    slug = forms.SlugField(
        label='Slug',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'product-name',
        })
    )

    description = forms.CharField(
        label='Oпис',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'rows': '3',
            'placeholder': 'Короткий опис ...',
        })
    )

    price = forms.DecimalField(
        label='Ціна',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'rows': '3',
            'placeholder': 'Ціна ...',
        })
    )

    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'description', 'price')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        gs = Product.objects.filter(name__iexact=name)
        if self.instance.pk:
            gs = gs.exclude(pk=self.instance.pk)
        if gs.exists():
            raise forms.ValidationError("Продукт з такою назвою існує.")
        return name