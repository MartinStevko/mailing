from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .models import *

connection = mail.get_connection()


class MailView(View):
    template = 'mailing/index.html'

    def get(self, request):
        print(connection)

        email = mail.EmailMessage(
            'Testovanie mailingu',
            'Ak tato sprava dojde, bude to fest dobre, lebo mailing mi zatial nikdy nesiel... :(',
            'postmaster@sandboxed4c14d561264981b491bdb1402da2c4.mailgun.org',
            ['mstevko10@gmail.com']
        )
        print(email)

        connection.open()
        email.send()

        # connection.send_messages([email])
        connection.close()
        return render(request, self.template)
