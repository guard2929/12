from django import forms
from django.contrib.auth.models import User
from .models import CPU, GPU, RAM, Storage, PCBuild


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
    cpu = forms.ModelChoiceField(
        queryset=CPU.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )
    gpu = forms.ModelChoiceField(
        queryset=GPU.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )
    ram = forms.ModelChoiceField(
        queryset=RAM.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )
    storage = forms.ModelChoiceField(
        queryset=Storage.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )

    class Meta:
        model = PCBuild
        fields = ['cpu', 'gpu', 'ram', 'storage', 'address']