from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from escola.viewsets import EscolaViewset, CursoViwset


router = routers.SimpleRouter()
router.register(r"", EscolaViewset, basename="escolas")

escolas_router = nested_routers.NestedSimpleRouter(router, r'', lookup='escolas')
escolas_router.register(r'cursos', CursoViwset)


urlpatterns = [

]

urlpatterns += router.urls
urlpatterns += escolas_router.urls