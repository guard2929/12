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
def build_form():
    return {
        'fields': {
            'cpu': CPU.objects.all(),
            'gpu': GPU.objects.all(),
            'ram': RAM.objects.all(),
            'storage': Storage.objects.all(),
        }
    }

@login_required
def configure_pc(request):
    cpus = CPU.objects.all()
    gpus = GPU.objects.all()
    rams = RAM.objects.all()
    storages = Storage.objects.all()

    if request.method == 'POST':
        selected_cpu = request.POST.getlist('cpu')
        selected_gpu = request.POST.getlist('gpu')
        selected_ram = request.POST.getlist('ram')
        selected_storage = request.POST.getlist('storage')

        build = PCBuild.objects.create(user=request.user)
        build.cpu.set(CPU.objects.filter(id__in=selected_cpu))
        build.gpu.set(GPU.objects.filter(id__in=selected_gpu))
        build.ram.set(RAM.objects.filter(id__in=selected_ram))
        build.storage.set(Storage.objects.filter(id__in=selected_storage))
        build.save()

        return render(request, 'store/configure_pc.html', {
            'success': True,
            'component_sections': [
                {'title': 'Процессоры', 'name': 'cpu', 'items': cpus},
                {'title': 'Видеокарты', 'name': 'gpu', 'items': gpus},
                {'title': 'Оперативная память', 'name': 'ram', 'items': rams},
                {'title': 'Накопители', 'name': 'storage', 'items': storages},
            ],
        })

    return render(request, 'store/configure_pc.html', {
        'component_sections': [
            {'title': 'Процессоры', 'name': 'cpu', 'items': cpus},
            {'title': 'Видеокарты', 'name': 'gpu', 'items': gpus},
            {'title': 'Оперативная память', 'name': 'ram', 'items': rams},
            {'title': 'Накопители', 'name': 'storage', 'items': storages},
        ]
    })

@login_required
def profile(request):
    all_builds = PCBuild.objects.filter(user=request.user)
    ordered_builds = all_builds.filter(is_ordered=True)
    drafts = all_builds.filter(is_ordered=False)

    return render(request, 'store/profile.html', {
        'ordered_builds': ordered_builds,
        'drafts': drafts,
    })
@login_required
def order_pc_build(request, build_id):
    build = get_object_or_404(PCBuild, id=build_id, user=request.user)
    if not build.is_ordered:
        build.is_ordered = True
        build.order_status = 'pending'
        build.save()
    return redirect('profile')
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import PCBuild

@login_required
def delete_build(request, build_id):
    build = get_object_or_404(PCBuild, id=build_id, user=request.user)
    if not build.is_ordered:
        build.delete()
    return redirect('profile')
