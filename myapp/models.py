from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return str(self.id) +'-' +self.name

class Movies(models.Model):
    movie_name = models.CharField(max_length=255, blank=True)
    movie_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    movie_poster = models.ImageField(blank=True, upload_to='movies/posters')
    year_released = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    imdb_rating = models.FloatField(blank=True)
    video_file = models.FileField(blank=True, upload_to='movies')

    def __str__(self):
        return str(self.id) +'-' +self.movie_name


class Episode(models.Model):
    title = models.CharField(max_length=255, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    video_file = models.FileField(blank=True, upload_to='episodes')

    def __str__(self):
        return str(self.id) +'-' +self.title

class Seasons(models.Model):
    season_number = models.IntegerField(blank=True)
    release_year = models.IntegerField(blank=True)
    number_of_episodes = models.IntegerField(blank=True)
    episodes = models.ManyToManyField(Episode)

    def __str__(self):
        return str(self.id) +'-' + str(self.season_number)

class Series(models.Model):
    series_poster = models.ImageField(blank=True, upload_to='series/posters')
    series_background_image = models.ImageField(blank=True, null=True, upload_to="series/bgi")
    name = models.CharField(max_length=255, blank=True)
    series_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seasons = models.ManyToManyField(Seasons)

    def __str__(self):
        return str(self.id) +'-' +self.name

