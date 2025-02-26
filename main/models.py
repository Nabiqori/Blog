from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    kasbi = models.CharField(max_length=255)
    yoshi = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Blog(models.Model):
    sarlavha = models.CharField(max_length=255)
    mavzu = models.CharField(max_length=255)
    matn = models.TextField(blank=True, null=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.mavzu

