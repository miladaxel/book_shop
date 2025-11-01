from django.contrib import admin
from home import models
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('categories',)


admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Author)