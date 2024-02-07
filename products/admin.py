from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'category']
    search_fields = ['name']
    ordering = ['name', 'price', 'category']



class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'create_timestamp']
    readonly_fields = ('create_timestamp',)
    extra = 0

