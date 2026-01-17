from django.apps import AppConfig

class ChatbotConfig(AppConfig):  # Changed from CoreConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'