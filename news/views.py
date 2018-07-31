from django.http import Http404, HttpResponse
from django.shortcuts import render
from news.models import News


def news_main(request):
    news_list = News.objects.all()
    return render(request, "news/news_main.html", {"news_list": news_list, })


def news_views(request, newsId):
    try:
        news = News.objects.get(pk=newsId)
    except News.DoesNotExist:
        raise Http404("News does not exist")
    return render(request, "news/news_views.html", {"news": news})
