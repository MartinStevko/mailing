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
        # connection.open()
        # email = mail.EmailMessage()
        # email.send()
        # or
        # connection.send_messages([email])
        # connection.close()
        print(connection)
        return render(request, self.template)
