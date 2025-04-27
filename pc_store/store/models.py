from django.db import models
from django.contrib.auth.models import User


class CPU(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='components/cpu/')

    def __str__(self):
        return self.name


class GPU(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='components/gpu/')

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='components/ram/')

    def __str__(self):
        return f"{self.name} ({self.capacity})"


class Storage(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='components/storage/')

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class PCBuild(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, null=True)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, null=True)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)


    def __str__(self):
        #print(self.user.username, self.created_at.strftime('%Y-%m-%d % H: %M'))
        #return f'''{self.user.username} ({self.created_at.strftime('%Y-%m-%d % H: %M')})'''
        return self.user.username

