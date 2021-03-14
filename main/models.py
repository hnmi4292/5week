from django.db import models


class Product(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.postname


class Get(models.Model):
    getname = models.CharField(max_length=50)
    photo = models.ImageField(blank=True, null=True)
    hopeprice = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.getname
