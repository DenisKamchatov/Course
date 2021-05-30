from django import template
from app.models import Categories

register = template.Library()


@register.simple_tag()
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('app/list_categories.html')
def show_categories():
    categories = Categories.objects.all()
    return {'categories': categories}
