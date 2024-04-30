from django.contrib import admin
from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns = [
   path('app2_test/',app2_test,name='app2_test'),
   path('app2_test2/',app2_test2,name='app2_test2'),
]