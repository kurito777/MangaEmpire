from rest_framework import viewsets
from .models import Author, Manga, TipoSubscripcion, Subscripcion
from .serializers import AuthorSerializer, MangaSerializer, TipoSubscripcionSerializer, SubscripcionSerializer
from django.shortcuts import render, redirect
from .forms import MangaForm


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

def subir_manga_view(request):
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manga')  # Redirige a la URL donde quieres ver el listado o los detalles del manga
    else:
        form = MangaForm()
    authors = Author.objects.all()  # Obtener todos los autores
    return render(request, 'subir_manga.html', {'form': form, 'authors': authors})
def manga_list_view(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_list.html', {'mangas': mangas})
def manga_list_view(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_list.html', {'mangas': mangas})

