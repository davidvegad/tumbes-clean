from django.contrib import admin
from .models import HeroSlide

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    list_editable = ('orden',)