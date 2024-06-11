from rest_framework import viewsets
from .models import Author, Manga, TipoSubscripcion, Subscripcion
from .serializers import AuthorSerializer, MangaSerializer, TipoSubscripcionSerializer, SubscripcionSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

class TipoSubscripcionViewSet(viewsets.ModelViewSet):
    queryset = TipoSubscripcion.objects.all()
    serializer_class = TipoSubscripcionSerializer

class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
