from django.shortcuts import render
from .models import PersonalInfo, Hobby

def home(request):
    personal_info = PersonalInfo.objects.first()  # Получаем первую запись
    hobbies = Hobby.objects.all()  # Получаем все записи хобби
    return render(request, 'home.html', {
        'personal_info': personal_info,
        'hobbies': hobbies,
    })
