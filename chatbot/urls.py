from django.urls import path
from . import views
app_name = 'chatbot'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('chat/', views.chat_home, name='chat_home'),
    path('chat/send/', views.send_message, name='send_message'),
    path('chat/clear/', views.clear_chat, name='clear_chat'),
]