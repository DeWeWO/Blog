from django.contrib import admin
from .models import Category, Post, PostImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")
    fields = ("id", "title", "slug", "description", "created", "updated")
    prepopulated_fields = {"slug": ("title", )}
    readonly_fields = ("id", "created", "updated")

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 2

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "author")
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ("title", "slug", "category")
    fields = ("id", "title", "slug", "description", "category", "author", "created", "updated")
    readonly_fields = ("id", "created", "updated")
    list_filter = ("created", "updated", "category")
    inlines = [PostImageAdmin]