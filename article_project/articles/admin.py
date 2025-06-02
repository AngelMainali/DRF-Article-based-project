from django.contrib import admin
from .models import Article


#admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at','author')
    search_fields=('title','content')
    list_filter=('created_at',)
admin.site.register(Article, ArticleAdmin)
