from django.urls import path
from Bng.views import *

app_name='Bng'

urlpatterns=[
    path('grand/',grand,name='grand'),
]