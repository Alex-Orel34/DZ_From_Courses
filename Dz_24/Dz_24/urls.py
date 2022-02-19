from django.contrib import admin
from django.urls import path
from Dz_24.views import index, show, save, send


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('show/', show),
    path('save/', save),
    path('send/', send)
]
