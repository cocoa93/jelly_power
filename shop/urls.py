from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
path('',views.shop_main),
path('support/',views.shop_support),
path('support/item/',views.shop_support_details),
path('goods/',views.shop_goods),
path('goods/item/',views.shop_goods_details),
        ]