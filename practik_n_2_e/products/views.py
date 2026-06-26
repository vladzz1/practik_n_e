import os
from django.shortcuts import get_object_or_404, render, redirect
from products.forms import ProductForm
from products.models import Product, ProductImage
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
                product.save()
                images = request.FILES.getlist('images')
                for index, image in enumerate(images):
                    ProductImage.objects.create(
                        product=product,
                        image=image,
                        priority=index
                    )
                messages.success(request, 'Product created successfully')
                return redirect('products:show_products')
            
            except Exception as x:
                messages.error(request, f'Помилка створення продукту {str(x)}')
        else:
            messages.error(request, 'Виправте помилки у формі')
    else:
        form = ProductForm()
    return render(request, 'products_create.html', { 'form': form })

def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            try:
                updated_product = form.save(commit=False)
                
                updated_product.save()

                new_images = request.FILES.getlist('images')
                if new_images:
                    old_images = updated_product.images.all()
                    for old_img in old_images:
                        if old_img.image and os.path.exists(old_img.image.path):
                            os.remove(old_img.image.path)
                    old_images.delete()
                    for index, image in enumerate(new_images):
                        ProductImage.objects.create(product=updated_product, image=image, priority=index)
                messages.success(request, 'Продукт успішно оновлено')
                return redirect('products:show_products')
                
            except Exception as x:
                messages.error(request, f'Помилка редагування продукту: {str(x)}')
        else:
            messages.error(request, 'Виправте помилки у формі')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'products_edit.html', {'form': form, 'product': product})

def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        try:
            product_images = product.images.all()
            
            for img_obj in product_images:
                if img_obj.image:
                    if os.path.exists(img_obj.image.path):
                        os.remove(img_obj.image.path)
            
            product.delete()
            messages.success(request, 'Продукт успішно видалено')
            
        except Exception as x:
            messages.error(request, f'Помилка при видаленні продукту: {str(x)}')
            
    return redirect('products:show_products')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products_details.html", {"product": product})