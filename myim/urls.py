
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path(r'', views.pajak.index),
    path(r'profil/', include('profil.urls')),
    path('admin/', admin.site.urls),
]
