from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='components/cpu/')

    def __str__(self):
        return self.name


class GPU(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='components/gpu/')

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='components/ram/')

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='components/storage/')

    def __str__(self):
        return self.name


class PCBuild(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.ManyToManyField('CPU')
    gpu = models.ManyToManyField('GPU')
    ram = models.ManyToManyField('RAM')
    storage = models.ManyToManyField('Storage')

    ORDER_STATUSES = [
        ('pending', 'Ожидает'),
        ('assembling', 'В сборке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
    ]
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUSES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сборка #{self.id} — {self.user.username}'
