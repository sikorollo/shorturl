from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/admin/', admin.site.urls),

    # Shortener Urls
    path('', include('urlshortener.urls'))
]