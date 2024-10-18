# main/admin.py

from django.contrib import admin
from .models import PersonalInfo, Hobby  # Импорт моделей

# Регистрация моделей
admin.site.register(PersonalInfo)
admin.site.register(Hobby)
