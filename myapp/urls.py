from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='homepage'),
    path('contact',views.contact,name='contactpage'),
]


