from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from serializers import *
from ..models import *


__all__ = [
    'MovieViewSet',
    'GenresViewSet',
    'LanguageViewSet',
    'CountryViewSet',
    'ActorViewSet',
    'CertificationViewSet'
]


class CertificationViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(type=data['type'])
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data={'name':data['name'] ,
                                                 'storyline':data['storyline'],
                                                 'genres':{data['genres']:data['genres']},
                                                 'certificate':data['certificate'],
                                                 'country':data['country'],
                                                 'language':data['language'],
                                                 'budget':data['budget'],
                                                 'actor':{data['actor']:data['actor']},
                                                 'director':{data['director']:data['director']},
                                                 'score':data['score']})
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
            except Exception as e:
                print("Error Raised:", e)
            return Response(serializer.data,status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        print("Data:",data)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(name=data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(fname=data['fname'],lname=data['lname'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GenresViewSet(viewsets.ModelViewSet):
    serializer_class = GenresSerializer

    def get_queryset(self):
        return Genres.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(name=data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return Language.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(name=data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

