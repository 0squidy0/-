from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date']
    list_filter = ['created_at']


    fieldsets = (
        ('Общие', {
            'fields': ['title', 'description', 'author'],
        }),
        ('Финансы', {
            'fields': ['price'],
            'classes': ['collapse']
        })
    )
admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.
