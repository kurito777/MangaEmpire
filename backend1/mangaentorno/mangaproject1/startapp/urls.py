from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, MangaViewSet, TipoSubscripcionViewSet, SubscripcionViewSet
from django.urls import path
from .views import subir_manga_view
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'mangas', MangaViewSet)
router.register(r'tiposubscripciones', TipoSubscripcionViewSet)
router.register(r'subscripciones', SubscripcionViewSet)


urlpatterns = [
    path('subir_manga/', subir_manga_view, name='subir_manga'),
   
]

urlpatterns = [
    path('', include(router.urls)),
]