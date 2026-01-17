from django.urls import path
from . import views
app_name = 'chatbot'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('', views.chat_home, name='chat_home'),
]