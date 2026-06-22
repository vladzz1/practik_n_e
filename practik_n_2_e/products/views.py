from django.shortcuts import render, redirect
from products.forms import ProductForm
from products.models import Product
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.
def show_products(request):
    products = Product.objects.prefetch_related("images").all()
    return render(request, "products.html", {"products": products})

def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                product = form.save(commit=False)
                if not product.slug:
                    product.slug = slugify(product.name, allow_unicode=False)
                # if 'image' in request.FILES:
                #     image = request.FILES['image']
                #     image_name = save_custom_image(image, size=(600,600), folder='categories')
                #     product.image=image_name
                product.save()
                messages.success(request, 'Product created successfully')
                return redirect('categories:list')
            
            except Exception as x:
                messages.error(request, f'Помилка створення продукту {str(x)}')
        else:
            messages.error(request, 'Виправте помилки у формі')
    else:
        form = ProductForm()
    return render(request, 'products_create.html', { 'form': form })