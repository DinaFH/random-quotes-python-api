
from django.urls import path

from .views import hello_drf,generate_all,generate_random

app_name='quotes-rest-v1'
urlpatterns=[
    path('hello-drf',hello_drf,name='ho-drf'),
    path('all',generate_all,name='gen-all'),
path('random',generate_random,name='gen-rand')
]