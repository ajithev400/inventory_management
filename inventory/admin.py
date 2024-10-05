from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at') 
    search_fields = ('name',)  
    ordering = ('created_at',)  


admin.site.register(Item, ItemAdmin)
