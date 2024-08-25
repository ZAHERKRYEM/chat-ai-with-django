from django.urls import path
from .views import chat,generate_response
app_name = "app"

urlpatterns = [
    path('',chat),
    path('generate_response/', generate_response, name='generate_response'),
    
]
