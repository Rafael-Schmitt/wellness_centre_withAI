from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings
import os

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
            
            # Check if OpenAI API key is available
            openai_api_key = os.environ.get('OPENAI_API_KEY', '')
            
            if not openai_api_key:
                # Provide helpful fallback responses
                fallback_responses = [
                    "Hello! I'm your tropical wellness assistant from Serenity Wellness Centre. For personalized wellness advice, please contact our center directly at hello@serenitywellness.com or call +55 (48) 3333-4444. Meanwhile, here's a wellness tip: Start your day with 5 minutes of beachfront meditation to reduce stress by up to 30%! 🌊",
                    "Aloha! 🌺 I'm currently in learning mode. For personalized tropical wellness guidance, our human experts are available at our Santa Catarina retreat. Try this: Take a mindful walk on the beach and practice gratitude for three things in nature around you.",
                    "Welcome to Serenity Wellness! While I'm upgrading my knowledge base, here's a tropical wellness tip: The sound of ocean waves naturally calms the nervous system. Spend 10 minutes listening mindfully today. For personalized programs, visit our center or contact us directly!"
                ]
                import random
                return JsonResponse({
                    'response': random.choice(fallback_responses)
                })
            
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=openai_api_key)
            
            # Create a wellness-focused prompt
            system_prompt = """You are a friendly, knowledgeable wellness assistant at Serenity Wellness Centre in Santa Catarina, Brazil. 
            You provide helpful, supportive, and professional advice about:
            - Tropical wellness practices
            - Beach yoga and meditation
            - Healthy eating with local Brazilian foods
            - Stress reduction techniques
            - Natural healing methods
            - Mindfulness in nature
            
            Keep responses warm, encouraging, and infused with tropical wellness wisdom.
            Mention elements like ocean, beach, rainforest, local fruits, and relaxation when appropriate.
            Always emphasize the healing power of nature and tropical environments.
            
            If someone asks about booking, prices, or specific appointments, politely direct them to contact the wellness center directly.
            """
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return JsonResponse({
                'response': response.choices[0].message.content
            })
            
        except Exception as e:
            # More user-friendly error message
            return JsonResponse({
                'response': "I'm having a moment of zen. 🌿 For immediate wellness advice, please contact our center directly or try asking about general wellness tips. Here's one: Practice deep breathing while visualizing ocean waves for instant relaxation."
            })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)