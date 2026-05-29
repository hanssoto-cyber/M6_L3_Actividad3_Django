from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-django/', views.sobre_django, name='sobre_django'),
    path('contacto/', views.contacto, name='contacto'),
]
