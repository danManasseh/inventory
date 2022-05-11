from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null= True)
    created = models.DateTimeField(auto_now_add=True)
    house_pic = models.ImageField(null = True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length = 200)
    home_name = models.ForeignKey(Home, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default = 0)
    item_img = models.ImageField(null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-updated','-created'] 

    def __str__(self):
        return self.name