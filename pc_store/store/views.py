from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CPU, GPU, RAM, Storage, PCBuild, Product
from .forms import RegisterForm, PCBuildForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('index')
    return render(request, 'store/delete_account.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # чтобы не выкидывало
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'store/change_password.html', {'form': form})


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
    selected_cpu=request.POST.getlist('cpu')
    selected_gpu = request.POST.getlist('gpu')
    selected_ram = request.POST.getlist('ram')
    selected_storage = request.POST.getlist('storage')
    success= False

    if request.method == 'POST':
        form = PCBuildForm(request.POST)
        if form.is_valid():
            pcbuild = form.save(commit=False)
            pcbuild.user = request.user
            pcbuild.save()
            success = True
            selected_cpu = selected_gpu = selected_ram = selected_storage = []
    else:
        form = PCBuildForm()
    context ={
        'form': form,
        'success' : success,
        'selected_cpu' : selected_cpu,
        'selected_gpu' : selected_gpu,
        'selected_ram' : selected_ram,
        'selected_storage' : selected_storage,
    }
    return render(request,'store/configure_pc.html', context)

@login_required
def profile_view(request):
    user_builds = PCBuild.objects.filter(user=request.user)
    return render(request, 'store/profile.html', {
        'user': request.user,
        'builds': user_builds,
    })
