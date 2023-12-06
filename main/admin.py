from django.contrib import admin

from main.models import Category, Content, Paragraphs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )


class ParagraphsInline(admin.TabularInline):
    fk_name = 'content'
    model = Paragraphs


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):

    fields = (('image', 'category'), )
    inlines = (ParagraphsInline,
    )
