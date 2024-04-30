

from django.contrib import admin
from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns = [
   path('app1_test/',app1_test,name='app1_test'),
   path('app1_test2/',app1_test2,name='app1_test2'),
]