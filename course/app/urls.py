from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('site/', site),
    path('categories/', categories, name="categories"),
    path('login/', login, name="login"),
    path('manufacturers/', manufacturers, name="manufacturers"),
    path('reviews/', reviews, name="reviews"),
    path('application/', application, name="application"),
    path('product/<int:product_id>', show_product, name="product"),
]
