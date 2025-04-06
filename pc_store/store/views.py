from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import RegisterForm, PCBuildForm


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "store/register.html", {"form": form})



@login_required
def configure_pc(request):
    success = False
    if request.method == "POST":
        form = PCBuildForm(request.POST)
        if form.is_valid():
            pc_build = form.save(commit=False)
            pc_build.user = request.user
            pc_build.save()
            success = True
    else:
        form = PCBuildForm()
    return render(request, "store/configure_pc.html", {"form": form, "success": success})
