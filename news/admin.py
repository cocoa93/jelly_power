from django.contrib import admin
from .models import News,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_created_date')

admin.site.register(News,PostAdmin)
admin.site.register(Comment)