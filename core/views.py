from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings
import os
import google.generativeai as genai
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services_list = [
        {
            'name': 'Beachfront Yoga',
            'description': 'Morning yoga sessions with ocean views and gentle sea breeze.',
            'icon': '🧘‍♀️',
            'class': 'yoga',
            'duration': '60-90 mins',
            'type': 'Group & Private',
            'price': '$45'
        },
        {
            'name': 'Ocean Therapy',
            'description': 'Healing sessions using the calming power of the ocean waves.',
            'icon': '🌊',
            'class': 'ocean',
            'duration': '45-60 mins',
            'type': 'Private',
            'price': '$65'
        },
        {
            'name': 'Tropical Massage',
            'description': 'Therapeutic massage using local oils and traditional techniques.',
            'icon': '💆',
            'class': 'massage',
            'duration': '60-120 mins',
            'type': 'Private',
            'price': '$85'
        },
        {
            'name': 'Meditation Retreat',
            'description': 'Guided meditation in our peaceful rainforest sanctuary.',
            'icon': '😌',
            'class': 'meditation',
            'duration': '30-60 mins',
            'type': 'Group & Private',
            'price': '$35'
        },
        {
            'name': 'Nutrition Guidance',
            'description': 'Personalized tropical nutrition plans with local superfoods.',
            'icon': '🥗',
            'class': 'nutrition',
            'duration': '60 mins',
            'type': 'Private',
            'price': '$55'
        },
        {
            'name': 'Forest Bathing',
            'description': 'Mindful walks through our protected rainforest trails.',
            'icon': '🌿',
            'class': 'forest',
            'duration': '90 mins',
            'type': 'Small Group',
            'price': '$40'
        },
    ]
    return render(request, 'services.html', {'services': services_list})

def contact(request):
    return render(request, 'contact.html')

def chatbot_view(request):
    return render(request, 'chatbot.html')

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Get Google Gemini API key from environment
            gemini_api_key = os.environ.get('GEMINI_API_KEY', '')
            
            if not gemini_api_key:
                # Fallback responses
                fallback_responses = [
                    "Hello! I'm your tropical wellness assistant from Serenity Wellness. For personalized advice, contact us at +55 (48) 3333-4444. 🌺",
                    "Welcome! I'm here to help with wellness tips. Try starting your day with beach meditation for stress relief!",
                ]
                import random
                return JsonResponse({
                    'response': random.choice(fallback_responses)
                })
            
            # Configure Gemini
            genai.configure(api_key=gemini_api_key)
            
            # Create the model
            model = genai.GenerativeModel('gemini-pro')
            
            # Create prompt
            prompt = f"""You are a friendly wellness assistant at Serenity Wellness Centre in Santa Catarina, Brazil. 
            You provide helpful, supportive advice about:
            - Tropical wellness practices
            - Beach yoga and meditation
            - Healthy eating with local Brazilian foods
            - Stress reduction techniques
            - Natural healing methods
            
            Keep responses warm, encouraging, and infused with tropical wellness wisdom.
            Mention elements like ocean, beach, rainforest, local fruits, and relaxation when appropriate.
            
            User question: {user_message}
            
            Your response:"""
            
            response = model.generate_content(prompt)
            
            return JsonResponse({
                'response': response.text
            })
            
        except Exception as e:
            return JsonResponse({
                'response': "I'm here to help with your wellness journey! For immediate assistance, please contact our center."
            })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)