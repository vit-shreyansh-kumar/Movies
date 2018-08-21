from rest_framework import serializers
from ..models import *

__all__ = ['MovieSerializer',
           'ActorSerializer',
           'GenresSerializer',
           'LanguageSerializer',
           'CountrySerializer',
           'CertificateSerializer']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'storyline', 'genres', 'certificate', 'country', 'language',
                  'budget', 'actor', 'director', 'score')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('fname','lname')


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('name',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name',)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('type',)