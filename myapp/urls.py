from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register("categories", views.CategoryViewset, basename="categories")
router.register("movies", views.MovieViewset, basename="movies")
router.register("episodes", views.EpisodeViewset, basename="episodes")
router.register("seasons", views.SeasonsViewset, basename="seasons")
router.register("series", views.SeriesViewset, basename="series")

urlpatterns = [
    path("", include(router.urls)),
    path("rec-sys/<str:movie>", views.recSys),
]
