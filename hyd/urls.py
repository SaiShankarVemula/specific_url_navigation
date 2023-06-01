from django.urls import path
from hyd.views import *

app_name='hyd'

urlpatterns=[
    path('bawarchi/',bawarchi,name='bawarchi'),
]