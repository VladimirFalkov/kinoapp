from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
)

app_name = "movie"

urlpatterns = [
    path("", MovieListView.as_view(), name="index"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/create/", MovieCreateView.as_view(), name="create_movie"),
    path(
        "movie/<int:pk>/update/",
        MovieUpdateView.as_view(),
        name="update_movie",
    ),
]
