from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:category_slug>', views.home, name="product_by_category"),
    path("category/<slug:category_slug>/<slug:product_slug>", views.productView, name="product_detail")
]