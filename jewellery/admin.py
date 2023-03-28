from django.contrib import admin
from .models import Category, Sub_Category, Product, Diamond

# Register your models here.

class PrdouctAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status', 'category', 'sub_category', 'favourite')
    list_display_links= ('id', 'name')
    list_filter= ('category',)
    ordering= ('id',)
    list_editable=('favourite',)
    
class DiamondAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shape','color', 'carat', 'clarity', 'price', 'status')
    list_display_links= ('id', 'name')
    ordering= ('id',)
    
    

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product, PrdouctAdmin)
admin.site.register(Diamond, DiamondAdmin)

