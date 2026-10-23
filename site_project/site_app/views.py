import requests
from django.conf import settings
from django.shortcuts import render


def movie_list(request):
    termo = request.GET.get("q", "").strip()

    filmes = []
    erro = None

    try:
        resposta = requests.get(
            settings.OMDB_URL,
            params={
                "apikey": settings.OMDB_API_KEY,
                "s": termo,
                "type": "movie",
            },
            timeout=10,
        )
        resposta.raise_for_status()
        dados = resposta.json()
        if dados.get("Response") == "True":
            filmes = dados.get("Search", [])
        else:
            erro = "Nenhum filme encontrado para essa busca."
    except requests.RequestException:
        erro = "Não foi possível acessar a API agora. Tente novamente em instantes."

    contexto = {"filmes": filmes, "termo": termo, "erro": erro}
    return render(request, "index.html", contexto)

# Create your views here.
