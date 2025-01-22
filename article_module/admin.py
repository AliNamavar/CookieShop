from django.contrib import admin
from . import models
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'is_active', 'slug')

    def save_model(self, request, obj: models.Article, form, change):
        if not change:
            obj.author = request.user

        super().save_model(request, obj, form, change)



admin.site.register(models.ArticleCategory)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.article_comments)
admin.site.register(models.ArticleVisited)