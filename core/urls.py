from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# Update this specific line below:
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls), # Note: corrected to .urls
    path('', include('transcriber.urls')),
] 

# This allows Django to serve files from the media folder during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)