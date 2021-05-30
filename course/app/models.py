from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    email = models.CharField('Почта', max_length=254)
    number = models.CharField('Телефон', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Product(models.Model):
    title = models.CharField('Название', max_length=254)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='photos/%Y/%m/%d/', null=True)
    price = models.CharField('Цена', max_length=100)  # Поменять CharField на что-то другое
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class Categories(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

