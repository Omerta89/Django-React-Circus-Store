from django.urls import path
from . import views
urlpatterns = [
     path('', views.index),
     path('products', views.products, name="products"),
     path('products/<id>', views.products, name="products"),


]

