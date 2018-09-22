from django.contrib import admin
from .models import *

'''
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'start_time', 'end_date', 'end_time', 'colored_name')
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Začiatok', {'fields': ('start_date', 'start_time'), }),
        ('Koniec', {'fields': ('end_date', 'end_time'), })
    )
    list_filter = ('start_date', 'end_date')

    search_fields = list_display
    ordering = ('-start_date', 'start_time', '-end_date', 'end_time')

admin.site.register(Event, EventAdmin)
'''
