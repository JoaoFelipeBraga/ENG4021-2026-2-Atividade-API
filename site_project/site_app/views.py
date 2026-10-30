import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Movie
from django.db.models import Q

def movie_list(request):
    termo = request.GET.get('q', '').strip()

    if termo:
        filmes = Movie.objects.filter(
            Q(title__icontains=termo) |
            Q(director__icontains=termo) |
            Q(genre__icontains=termo)
        )
    else:
        filmes = Movie.objects.all()

    contexto = {
        'filmes': filmes,
        'termo': termo
    }

    return render(request, 'index.html', contexto)

def create_movie(request):
    if request.method == "POST":
        Movie.objects.create(
            title = request.POST["title"],
            director = request.POST["director"],
            genre = request.POST["genre"],
            release_date = request.POST["release_date"],
        )
        return redirect("movie_list")
    return render(request, "forms.html", context={"action": "Adicionar"})

def update_movie(request, id):
    movie = Movie.objects.get(id = id)
    if request.method == "POST":
        movie.title = request.POST["title"]
        movie.director = request.POST["director"]
        movie.genre = request.POST["genre"]
        movie.release_date = request.POST["release_date"]
        movie.save()
        return redirect("movie_list")
    return render(request, "forms.html", context={"action": "Atualizar", "movie": movie})

def delete_movie(request, id):
    movie = Movie.objects.get(id = id)
    if request.method == "POST" and request.POST["confirm"]:
        movie.delete()
        return redirect("movie_list")
    return render(request, "confirmar.html", context={"action": "Deletar", "movie": movie})
# Create your views here.
