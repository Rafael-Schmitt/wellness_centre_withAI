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
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'response': 'Please enter a message! 🌺'})
            
            # Get API key from settings
            openai_api_key = settings.OPENAI_API_KEY
            
            if not openai_api_key:
                return JsonResponse({
                    'response': "🌿 Welcome to Serenity Wellness! Our AI assistant is currently upgrading. For personalized wellness advice, please contact us directly at hello@serenitywellness.com or call +55 (48) 3333-4444. Try our beachfront yoga sessions - they're amazing!"
                })
            
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=openai_api_key)
            
            # Enhanced system prompt
            system_prompt = """You are Luna, the friendly tropical wellness assistant at Serenity Wellness Centre in Santa Catarina, Brazil. 
            
            Your personality:
            - Warm, nurturing, and calming like ocean waves
            - Expert in tropical wellness, yoga, meditation, and natural healing
            - Always positive and encouraging
            - Use occasional tropical emojis 🌊🌺🌿☀️
            - Speak in a gentle, supportive tone
            
            Areas of expertise:
            1. Tropical wellness practices (beach yoga, ocean therapy, rainforest meditation)
            2. Brazilian superfoods and tropical nutrition
            3. Stress reduction and mindfulness techniques
            4. Natural healing methods using local resources
            5. Wellness routines for tropical climates
            
            Important rules:
            - If someone asks about booking, pricing, or appointments, respond: "For bookings and pricing, please contact our front desk at hello@serenitywellness.com or call +55 (48) 3333-4444"
            - Don't provide medical advice - suggest consulting with wellness professionals
            - Keep responses under 150 words
            - Focus on practical, actionable wellness tips
            - Mention local Brazilian elements when relevant
            - Never mention you're an AI - you're "Luna, the wellness guide"
            
            Example responses:
            - "The ocean breeze here in Santa Catarina is perfect for morning meditation! Try this: Find a quiet spot on the beach, close your eyes, and synchronize your breathing with the waves 🌊"
            - "For tropical nutrition, I love açai bowls with local fruits! They're packed with antioxidants and perfect for our climate."
            - "Beach yoga at sunrise is magical here! The combination of gentle movement, ocean sounds, and fresh air reduces stress naturally."
            """
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=300,
                temperature=0.8,
                top_p=0.9,
                frequency_penalty=0.3,
                presence_penalty=0.3
            )
            
            bot_response = response.choices[0].message.content.strip()
            
            return JsonResponse({
                'response': bot_response,
                'status': 'success'
            })
            
        except openai.APIError as e:
            return JsonResponse({
                'response': f"🌊 Our wellness connection is taking a mindful pause. Please try again in a moment or contact us directly for assistance."
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'response': 'Please send your wellness question in the proper format.'
            })
        except Exception as e:
            print(f"Chat error: {str(e)}")  # For debugging
            return JsonResponse({
                'response': "🌿 Welcome to Serenity Wellness! I'm here to share tropical wellness wisdom. How can I help you find peace and balance today?"
            })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
