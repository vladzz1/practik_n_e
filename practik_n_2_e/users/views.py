from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import CustomUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            return redirect('homepage')
        else:
            messages.info(request, 'Виникли помилки при заповненні форми')
    else:
        form = CustomUserForm()

    return render(request, "register.html", {"form": form})