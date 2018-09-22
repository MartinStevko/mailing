from django.urls import path

from .views import MailView

app_name = 'mailing'

urlpatterns = [
    path('', MailView.as_view(), name='index'),
]
