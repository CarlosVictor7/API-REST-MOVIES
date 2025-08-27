from rest_framework import viewsets, filters
from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "genre"]
    ordering_fields = ["id", "title", "release_year", "rating", "created_at"]
    ordering = ["-created_at"]
