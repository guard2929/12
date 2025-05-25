from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CPU, GPU, RAM, Storage, PCBuild, Product, PrebuiltOrder
from .forms import RegisterForm, PCBuildForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib import messages

def about(request):
    return render(request, 'store/about.html')

def faq(request):
    return render(request, 'store/faq.html')

def contacts(request):
    return render(request, 'store/contacts.html')

def privacy_policy(request):
    return render(request, 'store/privacy_policy.html')

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
def order_prebuilt(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    PrebuiltOrder.objects.create(user=request.user, product=product)
    return redirect('profile')
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

        if not selected_cpu or not selected_ram:
            messages.error(request, "Пожалуйста, выберите хотя бы один процессор и одну планку оперативной памяти.")
            return render(request, 'store/configure_pc.html', {
                'cpus': cpus,
                'gpus': gpus,
                'rams': rams,
                'storages': storages,
            })

        build = PCBuild.objects.create(user=request.user)
        build.cpu.set(CPU.objects.filter(id__in=selected_cpu))
        build.gpu.set(GPU.objects.filter(id__in=selected_gpu))
        build.ram.set(RAM.objects.filter(id__in=selected_ram))
        build.storage.set(Storage.objects.filter(id__in=selected_storage))
        build.save()

        messages.success(request, "Сборка успешно сохранена!")
        return redirect('profile')

    return render(request, 'store/configure_pc.html', {
        'cpus': cpus,
        'gpus': gpus,
        'rams': rams,
        'storages': storages,
    })

@login_required
def profile(request):
    all_builds = PCBuild.objects.filter(user=request.user)
    ordered_builds = all_builds.filter(is_ordered=True)
    drafts = all_builds.filter(is_ordered=False)
    prebuilt_orders = PrebuiltOrder.objects.filter(user=request.user)

    return render(request, 'store/profile.html', {
        'ordered_builds': ordered_builds,
        'drafts': drafts,
        'prebuilt_orders': prebuilt_orders,
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
@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')
