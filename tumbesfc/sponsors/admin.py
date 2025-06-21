from django.contrib import admin
from .models import Sponsor

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'destacado')
    list_filter = ('destacado',)
