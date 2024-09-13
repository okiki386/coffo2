from django.contrib import admin
from .models import BlogPost
from .models import Product

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_date', 'image')
    list_filter = ('title', 'created_date')

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'created_at', 'image')
    list_filter = ('name', 'price', 'created_at')
    list_per_page =40

