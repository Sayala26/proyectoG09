
from authApp.views.alimento_view.alimentoViewSet import AlimentoViewSet
from rest_framework import routers
from authApp.views.limpieza_view.limpiezaViewSet import LimpiezaViewSet
from authApp.views.proveedor_view.proveedorViewSet import ProveedorViewSet


router = routers.DefaultRouter()
router.register('alimento', AlimentoViewSet)
router.register('limpieza',LimpiezaViewSet)
router.register('proveedor',ProveedorViewSet)

