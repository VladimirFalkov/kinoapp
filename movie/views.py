from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Movie
from .forms import MovieForm


class MovieListView(ListView):
    model = Movie
    template_name = "movie/index.html"
    context_object_name = "movies"
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(description__icontains=search_query)
            )
        ordering = self.request.GET.get("ordering")

        if ordering == "year":
            queryset = queryset.order_by("year_released")
        elif ordering == "genre":
            queryset = queryset.order_by("genre")
        elif ordering == "rating":
            queryset = queryset.order_by("-rating")
        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/detail.html"
    context_object_name = "movie"


class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie/create_movie.html"
    form_class = MovieForm
    success_url = reverse_lazy("movie:index")


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie/create_movie.html"
    success_url = reverse_lazy("movie:index")
