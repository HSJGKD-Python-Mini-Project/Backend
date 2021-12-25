# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from .recSys import get_sorted_recommendations
from myapp.models import Category, Movies, Episode, Seasons, Series
from myapp.serializers import (
    CategorySerializer,
    MoviesSerializer,
    EpisodeSerializer,
    SeasonsSerializer,
    SeriesSerializer,
)
import json
from random import shuffle


# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

    @action(detail=True, methods=["get"])
    def movies(self, request, pk=None):
        category = self.get_object()
        movies = Movies.objects.filter(movie_category=category)
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def series(self, request, pk=None):
        category = self.get_object()
        series = Series.objects.filter(series_category=category)
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    @action(detail=False, methods=["get"])
    def trending(self, request):
        movies = Movies.objects.all()
        movies = list(movies)
        shuffle(movies)
        serializer = MoviesSerializer(movies[:10], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def popular(self, request, pk=None):
        movies = Movies.objects.all().order_by("-imdb_rating")[:10]
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EpisodeViewset(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class SeasonsViewset(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer


class SeriesViewset(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    @action(detail=False, methods=["get"])
    def trending(self, request):
        series = Series.objects.all()
        series = list(series)
        shuffle(series)
        serializer = SeriesSerializer(series[:11], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def recSys(request, movie):
    return Response(json.dumps(get_sorted_recommendations(movie)))
