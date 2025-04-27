from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class PCBuild(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #print(self.user.username, self.created_at.strftime('%Y-%m-%d % H: %M'))
        #return f'''{self.user.username} ({self.created_at.strftime('%Y-%m-%d % H: %M')})'''
        return self.user.username

