from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, MangaViewSet, TipoSubscripcionViewSet, SubscripcionViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'mangas', MangaViewSet)
router.register(r'tiposubscripciones', TipoSubscripcionViewSet)
router.register(r'subscripciones', SubscripcionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]