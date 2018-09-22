from django.db import models
from django.utils import timezone

'''
class Event(models.Model):
    name = models.CharField(max_length=30, verbose_name='názov')
    text = HTMLField(verbose_name='obsah článku')
    start_date = models.DateField(default=timezone.now, verbose_name='začiatok (dátum)')
    end_date = models.DateField(null=True, blank=True, verbose_name='koniec (dátum)')
    start_time = models.TimeField(null=True, blank=True, verbose_name='začiatok (čas)')
    end_time = models.TimeField(null=True, blank=True, verbose_name='koniec (čas)')

    def __str__(self):
        return self.name

    def colored_name(self):
        return format_html(
            '<span style="color: #ff7777;">{}</span>',
            self.name,
        )

    class Meta:
        verbose_name = 'udalosť'
        verbose_name_plural = 'udalosti'
'''
