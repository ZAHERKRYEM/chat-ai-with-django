from django.shortcuts import render
from django.http import JsonResponse

from groq import Groq
# Create your views here.
client = Groq(
    api_key='<api_key>',
)


def chat(request):
    return render(request, 'chatgpt.html')

def generate_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": user_message,
        }
        ],
        model="llama3-8b-8192",)

        return JsonResponse({'response': chat_completion.choices[0].message.content})
