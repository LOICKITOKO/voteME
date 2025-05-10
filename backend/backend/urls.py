from django.conf import settings
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vote_app.urls')),
    path('', lambda request: JsonResponse({"message": "Bienvenue sur l'API VoteME"})),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
