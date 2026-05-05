from django.shortcuts import render
from .models import Transcription
from faster_whisper import WhisperModel
import os

# Load model ONCE globally (outside the view) to save time
# 'int8' quantization makes it much faster on CPU
model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_obj = Transcription.objects.create(audio_file=request.FILES['audio'])
        
        # transcribe returns a generator of segments
        segments, info = model.transcribe(audio_obj.audio_file.path, beam_size=5)
        
        # Combine all segments into one full string
        full_text = "".join([segment.text for segment in segments])
        
        audio_obj.transcript_text = full_text.strip()
        audio_obj.save()
        
        return render(request, 'result.html', {'transcription': audio_obj})
    
    return render(request, 'upload.html')