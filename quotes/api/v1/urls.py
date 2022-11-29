
from django.urls import path

from .views import generate_all,generate_random

app_name='quotes-rest-v1'
urlpatterns=[
    path('all',generate_all,name='gen-all'),
    path('random',generate_random,name='gen-rand')
]