from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('api/chat/', views.chat_api, name='chat_api'),
]