from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    image = models.ImageField(upload_to='media/category/', verbose_name='Излюоажение категории')
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Promotions(models.Model):
    name = models.CharField(max_length=155)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    descriprion = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name
