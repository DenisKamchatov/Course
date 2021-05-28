from django.contrib import admin
from .models import Categories, Product, User


class CategoriesAdmin(admin.ModelAdmin):
    list_display = 'title'
    search_fields = 'title'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')


admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
