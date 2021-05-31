from django.db import models
from django.db.models.base import Model
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
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Категории')
    slug = models.SlugField(max_length=254, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


class Categories(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField(max_length=254, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Reviews(models.Model):
    name = models.CharField('Имя', max_length=150)
    surname = models.CharField('Фамилия', max_length=150)
    text = models.TextField('Текст отзыва')
    image = models.ImageField('Картинка пользователя', upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Application(models.Model):
    name = models.CharField('Имя', max_length=150)
    surname = models.CharField('Фамилия', max_length=150)
    number = models.CharField('Номер телефона', max_length=100)
    email = models.CharField('Почта', max_length=254)
    text = models.TextField('Текст заявки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Subscription(models.Model):
    email = models.CharField('Почта', max_length=254)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'