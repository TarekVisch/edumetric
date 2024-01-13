from django.urls import path
from . import views

urlpatterns = [
    path('', views.tacher_home, name='tacher_home'),
]
