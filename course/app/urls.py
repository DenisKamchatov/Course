from django.urls import path

from .views import *

urlpatterns = [
    path('', site, name="home"),
    path('category/<int:cat_id>', show_category, name="category"),
    path('reviews/', reviews, name="reviews"),
    path('application/', application, name="application"),
    path('login/', login, name="login"),

    # path('site/', index),
    # path('categories/', categories, name="categories"),
    # path('manufacturers/', manufacturers, name="manufacturers"),
    
    # path('product/<int:product_id>', show_product, name="product"),
]
