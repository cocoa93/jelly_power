from django.urls import path
from . import views

app_name = "staticpages"
urlpatterns = [
path('', views.index),
path('about/', views.about),
path('join/', views.join),
path('join/welcome',views.welcome)

]