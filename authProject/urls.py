from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
from authApp.views.cocina_view.cocinaViewSet import CocinaViewSet
from authApp.views.alimento_view.alimentoViewSet import AlimentoViewSet
from authApp.views.proveedor_view.proveedorViewSet import ProveedorViewSet
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS CAMILO
    path('login/', TokenObtainPairView.as_view()), # ejemplo de login con tokens
    path('refresh/', TokenRefreshView.as_view()), # token refresh
    path('user/', views.UsuarioCreateView.as_view()), # crear usuario

    # URL ANGIE
    path('alimentos/', include(router.urls)), #CRUD Alimentos
    #path('Alimento/<int:pk>', AlimentoViewSet.as_view({'get':'retrieve', 'patch':'partial_update', 'put': 'update'})),
    #path('Alimento/list', AlimentoViewSet.as_view({'get':'list'})),
    #path('Alimento/create', AlimentoViewSet.as_view({'post':'create'})),
    #path('Alimento/delete/<int:pk>', AlimentoViewSet.as_view({'delete':'destroy'})),


    #URLS ALEJANDRA
    path('cocina/<int:pk>', CocinaViewSet.as_view({'get':'retrieve', 'patch':'partial_update', 'put': 'update'})),
    path('cocina/list', CocinaViewSet.as_view({'get':'list'})),
    path('cocina/create', CocinaViewSet.as_view({'post':'create'})),
    path('cocina/delete/<int:pk>', CocinaViewSet.as_view({'delete':'destroy'})),

    #URLS BRANDON
    path('proveedor/<int:pk>', ProveedorViewSet.as_view({'get':'retrieve', 'patch':'partial_update', 'put': 'update'})),
    path('proveedor/list', ProveedorViewSet.as_view({'get':'list'})),
    path('proveedor/create', ProveedorViewSet.as_view({'post':'create'})),
    path('proveedor/delete/<int:pk>', ProveedorViewSet.as_view({'delete':'destroy'})),


]
