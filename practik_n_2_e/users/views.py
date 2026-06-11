from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import CustomUserRegisterForm, CustomUserLoginForm
from .utils import save_custom_image
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                if 'email' in form.changed_data:
                    user.username = form.cleaned_data['email']
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    user.image_small = save_custom_image(image,size=(300,300), folder='small')
                    user.image_medium = save_custom_image(image,size=(800,800), folder='medium')
                    user.image_large = save_custom_image(image,size=(1200,1200), folder='large')
                user.save()
                login(request, user)
                return redirect('homepage')
            except Exception as x:
                messages.error(request, f'Щось пішло не так: {str(x)}')
        else:
            messages.info(request, 'Виникли помилки при заповненні форми')
    else:
        form = CustomUserRegisterForm()

    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage')