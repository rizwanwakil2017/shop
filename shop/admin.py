from django.contrib import admin
from .models import Catalog, Category, Product, ProductDetail, ProductAttribute

# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'publisher', 'description', 'pub_date']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Catalog, CatalogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display =['product', 'attribute', 'value', 'description']
admin.site.register(ProductDetail, ProductDetailAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(ProductAttribute, ProductAttributeAdmin)