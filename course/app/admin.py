from django.contrib import admin
from .models import Categories, Product, User, Application, Reviews, Subscription


class CategoriesAdmin(admin.ModelAdmin):
    list_display = 'title'
    search_fields = 'title'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'number', 'email')
    search_fields = ('name', 'surname')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'number', 'email', 'text')
    search_fields = ('name', 'surname')


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
