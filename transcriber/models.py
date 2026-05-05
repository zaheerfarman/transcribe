from django.db import models


class Transcription(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    transcript_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)