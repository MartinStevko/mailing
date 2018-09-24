from django.shortcuts import render, redirect
from django.views import View

from django.conf import settings
from django.core.mail import send_mail
from .models import *


class MailView(View):
    template = 'mailing/index.html'

    def get(self, request):
        send_mail(
            'Testovanie mailingu',
            'Ak tato sprava dojde, bude to fest dobre, lebo mailing mi zatial nikdy nesiel... :(',
            settings.EMAIL_HOST_USER,
            ['mstevko10@gmail.com'],
            fail_silently=False
        )
        return render(request, self.template)
