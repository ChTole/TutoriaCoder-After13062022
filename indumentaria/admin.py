from django.contrib import admin

from .models import Remera

class RemeraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'talle', 'color', 'precio')

admin.site.register(Remera, RemeraAdmin)
