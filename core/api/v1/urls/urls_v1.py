from django.urls import path
from core.api.v1.views.views_v1 import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('index/', index ),
]