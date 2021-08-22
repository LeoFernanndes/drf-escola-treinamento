from rest_framework import routers
from escola.viewsets import EscolaViewset

router = routers.SimpleRouter()
router.register(r"", EscolaViewset, basename="escolas")

urlpatterns = [

]

urlpatterns += router.urls