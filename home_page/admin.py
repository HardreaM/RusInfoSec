from django.contrib import admin
from .models import Rubric
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Rubric)