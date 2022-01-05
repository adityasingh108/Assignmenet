from django.contrib import admin
from . models import product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name',]
admin.site.register(product)
