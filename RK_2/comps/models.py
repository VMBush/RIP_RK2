from django.db import models
import os

# Create your models here.
class Computer(models.Model):
    model = models.CharField(max_length=50, verbose_name=("Модель"), null=True)
    count = models.CharField(max_length=10, verbose_name=("Количество"), default='0')
    classroom = models.ForeignKey("class", verbose_name=("Класс"), on_delete=models.CASCADE, null=True)
    

    class Meta:
        verbose_name = ("Computer")
        verbose_name_plural = ("Computers")

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("Computer_detail", kwargs={"pk": self.pk})

class Class(models.Model):

    name = models.CharField(max_length=50, verbose_name=("Название"), null=True)

    class Meta:
        verbose_name = ("Class")
        verbose_name_plural = ("Classes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Class_detail", kwargs={"pk": self.pk})

