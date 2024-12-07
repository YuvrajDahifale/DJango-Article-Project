from django.contrib import admin
from .models import Article

# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display=['title','slug','author','created_date','body']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Article,AdminArticle)