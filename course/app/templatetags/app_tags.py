from django import template
from app.models import Categories, Reviews

register = template.Library()


@register.simple_tag()
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('app/list_categories.html')
def show_categories(cat_selected = 0):
    categories = Categories.objects.all()
    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag('app/list_menu.html')
def show_menu():
    menu = [
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
    {'title': 'Оставить заявку', 'url_name': 'application'},    
    ]
    return {'menu': menu}


@register.inclusion_tag('app/reviews.html')
def get_reviews():
    new = Reviews.objects.all()[:3]
    return {'new': new}


@register.inclusion_tag('app/get_site_reviews.html')
def show_reviews():
    reviews = Reviews.objects.all()
    return {'reviews': reviews}