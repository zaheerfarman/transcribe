from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcribe_audio, name='upload_audio'),
]