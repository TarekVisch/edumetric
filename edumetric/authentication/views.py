from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
