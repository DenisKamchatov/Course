from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def site(request):
    catalog = Product.objects.all()
    context = {
        'title': 'Сорт',
        'catalog': catalog,
        'cat_selected': 0,
    }
    return render(request, 'app/index.html', context=context)


def show_category(request, cat_id):
    catalog = Product.objects.filter(cat_id=cat_id)
    context = {
        'catalog': catalog,
        'cat_selected': cat_id,
    }
    return render(request, 'app/index.html', context=context)


def entry(request):
    user = User.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'app/entry.html', context=context)


def reviews(request):
    return render(request, 'app/site_reviews.html')


def application(request):
    return HttpResponse('Оставить заявку')


def login(request):
    return HttpResponse('Войти')


# def manufacturers(request):
#     return HttpResponse('Производители')


# def show_product(request, product_id):
#     return HttpResponse(f'id продукта: { product_id }')


# def categories(request):
#     category = Categories.objects.all()
#     content = {
#         'title': 'Категории',           # Чтобы не писать все это в одну строчку можно создать массив
#         'categories': category,         # и в render уже прописать свойство context
#     }
#     return render(request, 'app/categories.html', context=content)

# def index(request):
#     catalog = Product.objects.all()
#     context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'catalog': catalog,
#     }
#     return render(request, 'app/base.html', context=context)

