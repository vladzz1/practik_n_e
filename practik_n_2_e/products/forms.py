from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    category = forms.CharField(
        label='Назва категорії',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'placeholder': 'Назва категорії ...',
        })
    )

    name = forms.CharField(
        label='Назва продукту',
        max_length=100,
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
            'placeholder': 'category-name',
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

    price = forms.CharField(
        label='Ціна',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
            'rows': '3',
            'placeholder': 'Ціна ...',
        })
    )

    # created_at = forms.CharField(
    #     label='Створено в',
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
    #         'rows': '3',
    #         'placeholder': 'Створено в ...',
    #     })
    # )

    # updated_at = forms.CharField(
    #     label='Оновлено в',
    #     required=False,
    #     widget=forms.TextInput(attrs={
    #         'class': 'w-full rounded-lg border border-gray-700 bg-gray-900 px-4 py-3 text-white placeholder-gray-500 focus:border-indigo-500 focus:outline-none',
    #         'rows': '3',
    #         'placeholder': 'Оновлено в ...',
    #     })
    # )

    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'description', 'price', 'created_at', 'updated_at')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        gs = Product.objects.filter(name=name)
        if self.instance.pk:
            gs = gs.exclude(pk=self.instance.pk)
        if gs.exists():
            raise forms.ValidationError("Продукт з такою назвою існує.")
        return name