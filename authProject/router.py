from authApp.views.alimento_view.alimentoViewSet import AlimentoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alimento', AlimentoViewSet)

