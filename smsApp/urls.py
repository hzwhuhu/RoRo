from django.urls import path

from smsApp import apis

urlpatterns = [
    path('sms/', apis.sms),
    path('login/', apis.login)
]
