from . import views
from django.urls import path

appName = 'ElectionCode'

urlpatterns=[
    path('', views.index, name="index")
]