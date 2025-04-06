from django import forms
from django.contrib.auth.models import User
from .models import PCBuild


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
    class Meta:
        model = PCBuild
        fields = ['cpu', 'gpu', 'ram', 'storage', 'address']
        widgets = {
            'cpu': forms.Select(choices=[
                ('Intel i5', 'Intel i5'),
                ('Intel i7', 'Intel i7'),
                ('AMD Ryzen 5', 'AMD Ryzen 5'),
                ('AMD Ryzen 7', 'AMD Ryzen 7'),
            ]),
            'gpu': forms.Select(choices=[
                ('NVIDIA RTX 3060', 'NVIDIA RTX 3060'),
                ('NVIDIA RTX 4060', 'NVIDIA RTX 4060'),
                ('AMD RX 6700 XT', 'AMD RX 6700 XT'),
            ]),
            'ram': forms.Select(choices=[
                ('16 ГБ', '16 ГБ'),
                ('32 ГБ', '32 ГБ'),
            ]),
            'storage': forms.Select(choices=[
                ('SSD 512 ГБ', 'SSD 512 ГБ'),
                ('SSD 1 ТБ', 'SSD 1 ТБ'),
            ]),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите адрес доставки'}),
        }