
from authApp.views.alimento_view.alimentoViewSet import AlimentoViewSet
from rest_framework import routers
from authApp.views.limpieza_view.limpiezaViewSet import LimpiezaViewSet


router = routers.DefaultRouter()
router.register('alimento', AlimentoViewSet)
router.register('limpieza',LimpiezaViewSet)

