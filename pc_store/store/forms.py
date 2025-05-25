from django import forms
from django.contrib.auth.models import User
from .models import CPU, GPU, RAM, Storage, PCBuild, Product


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', "Пароли не совпадают")

class PCBuildForm(forms.ModelForm):
    cpu = forms.ModelMultipleChoiceField(
        queryset=CPU.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    gpu = forms.ModelMultipleChoiceField(
        queryset=GPU.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    ram = forms.ModelMultipleChoiceField(
        queryset=RAM.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    storage = forms.ModelMultipleChoiceField(
        queryset=Storage.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = PCBuild
        fields = ['cpu', 'gpu', 'ram', 'storage']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']