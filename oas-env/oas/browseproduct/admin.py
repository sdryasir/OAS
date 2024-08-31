from django.contrib import admin
from .models import cards

  




class items(admin.ModelAdmin):
    list_display = ['title','text','price','image']

admin.site.register(cards,items)   
