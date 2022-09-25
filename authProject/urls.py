from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS CAMILO
    path('login/', TokenObtainPairView.as_view()), # ejemplo de login con tokens
    path('refresh/', TokenRefreshView.as_view()), # token refresh
    path('user/', views.UsuarioCreateView.as_view()), # crear usuario
    path('user/<int:pk>/', views.UsuarioReadView.as_view()), # leer usuario
]
