from django.urls import path
from . import views


app_name = "mypage"
urlpatterns = [
path('',views.mypage),
path('wish_list',views.wish_list),
path('cart',views.cart)
        ]