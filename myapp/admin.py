from django.contrib import admin
from .models import *


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'uploaded', 'modified', 'video_file']
admin.site.register(Episode, EpisodeAdmin)

class SeasonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'season_number', 'release_year', 'number_of_episodes', 'get_episodes']

    def get_episodes(self, obj):
        return ", ".join([p.title for p in obj.episodes.all()])
admin.site.register(Seasons, SeasonsAdmin)

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['id','series_poster','name','series_category', 'get_seasons']
    def get_seasons(self, obj):
        return ", ".join([str(p.season_number) for p in obj.seasons.all()])
admin.site.register(Series, SeriesAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie_name', 'movie_category', 'movie_poster', 'year_released', 'description', 'imdb_rating', 'video_file']
admin.site.register(Movies, MovieAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Category, CategoryAdmin)