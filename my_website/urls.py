# my_website/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#My name is Alex and i like sport, fast cars and programming.

#I like to lift weights my BP are 120 kg | 264,5 lbs

#Traning

#Alexander Burmitskiy

