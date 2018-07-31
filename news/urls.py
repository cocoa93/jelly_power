from django.urls import path
from . import views


app_name = "news"
urlpatterns = [
path('',views.news_main,name="news_main"),
path('<int:newsId>/', views.news_views, name="news_views"),

#path('<int:pk>/comments/new/',views.comment_new),

        ]