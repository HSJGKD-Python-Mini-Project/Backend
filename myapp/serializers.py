from django.db.models import fields
from rest_framework import serializers
from accounts.models import User
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class MoviesSerializer(serializers.ModelSerializer):
    movie_category = CategorySerializer()

    class Meta:
        model = Movies
        fields = [
            "id",
            "movie_name",
            "movie_category",
            "year_released",
            "description",
            "imdb_rating",
            "video_file",
            "movie_poster",
        ]


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ["id", "title", "uploaded", "modified", "video_file"]


class SeasonsSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer()

    class Meta:
        model = Seasons
        fields = [
            "id",
            "season_number",
            "release_year",
            "number_of_episodes",
            "episodes",
        ]


class SeriesSerializer(serializers.ModelSerializer):
    series_category = CategorySerializer()
    seasons = SeasonsSerializer(many=True)

    class Meta:
        model = Series
        fields = [
            "id",
            "name",
            "series_category",
            "seasons",
            "series_poster",
            "series_background_image",
        ]
