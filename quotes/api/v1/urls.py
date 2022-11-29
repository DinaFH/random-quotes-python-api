
from django.urls import path
from .views import hello_drf

app_name='quotes-rest-v1'
urlpatterns=[
    path('hello-drf',hello_drf,name='ho-drf')
]