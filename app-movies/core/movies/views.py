#We import the libraries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie
from .serializers import MovieSerializer

# We generate a JSON type response.
def index_movies(request):
    return JsonResponse({"message": "online"})

# We declare our view for Movie.
class MovieView(APIView):
    # Definition of the GET method.
    def get(self, request, pk = None):
        if pk:
            #movie = Movie.objects.get(pk=pk)
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieSerializer(movie)
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)

    # POST method definition
    def post(self, request):
        # JSON of the request
        print(request.data)
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Definition of the PUT method.
    def put(self, request, pk = None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, states = status.HTTP_400_BAD_REQUEST)
    
    # Definition of the DELETE method.
    def delete(self, request, pk = None):
        if pk: 
            movie = get_object_or_404(Movie, pk=pk)
            movie.delete()
        else:
            return Response(
                {"msg": "Necesitas enviar el ID de la pelicula a eliminar"},
                status = status.HTTP_400_BAD_REQUEST
                )
        return Response({"msg": "Pelicula con ID {} eliminado"})