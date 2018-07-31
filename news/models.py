from django.db import models
# Create your models here.
from django.utils import timezone


class News(models.Model):
    news_id = models.IntegerField(primary_key=True, auto_created=True)
    news_title = models.CharField(max_length=100)
    news_text = models.TextField()
    news_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.news_title

class NewsImg(models.Model):
    img_id = models.IntegerField(primary_key=True, auto_created=True)
    img_news = models.ForeignKey(News, on_delete=models.CASCADE)
    img_item = models.ImageField(blank=True, null=True)

class Comment(models.Model):
    com_post = models.ForeignKey(News, on_delete=models.CASCADE)
    com_text = models.TextField()
    com_author = models.CharField(max_length=10)
    com_created_date = models.DateTimeField(auto_now_add=True)

