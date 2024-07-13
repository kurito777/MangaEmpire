from rest_framework import serializers
from .models import Author, Manga, TipoSubscripcion, Subscripcion
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name', 'bith_date']

class MangaSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)

    class Meta:
        model = Manga
        fields = ['idManga', 'title', 'author_id', 'estado']

    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        author = Author.objects.get(pk=author_id)
        manga = Manga.objects.create(author=author, **validated_data)
        return manga

class TipoSubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSubscripcion
        fields = ['id', 'nombre', 'descripcion', 'precio']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class SubscripcionSerializer(serializers.ModelSerializer):
    tipo = TipoSubscripcionSerializer()
    usuario = UserSerializer()

    class Meta:
        model = Subscripcion
        fields = ['id', 'tipo', 'usuario', 'fecha_inicio', 'fecha_fin']

    def create(self, validated_data):
        tipo_data = validated_data.pop('tipo')
        usuario_data = validated_data.pop('usuario')

        # Obtener el tipo de subscripción existente o crear uno nuevo si no existe
        tipo_subscripcion = TipoSubscripcion.objects.get_or_create(**tipo_data)[0]

        # Obtener el usuario existente o crear uno nuevo si no existe
        usuario = User.objects.get_or_create(**usuario_data)[0]

        subscripcion = Subscripcion.objects.create(
            tipo=tipo_subscripcion,
            usuario=usuario,
            **validated_data
        )
        return subscripcion

