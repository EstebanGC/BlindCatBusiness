from django.urls import path, include
from rest_framework import routers
from blindcatb import views

product_router = routers.DefaultRouter()
product_router.register(r"products", views.ProductView, "products")
buy_router = routers.DefaultRouter()
buy_router.register(r'buys', views.BuyView, 'buys')

urlpatterns = [
    path("api/v1/", include(product_router.urls)),
    path("api/v1/", include(buy_router.urls)),
]
#All of the code above, generates all crud requests

