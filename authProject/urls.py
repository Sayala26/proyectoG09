from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS CAMILO
    path('login/', TokenObtainPairView.as_view()), # ejemplo de login con tokens
    path('refresh/', TokenRefreshView.as_view()), # token refresh
    path('user/', views.UsuarioCreateView.as_view()), # crear usuario

    path('api/', include(router.urls)) #CRUD Alimentos

]
