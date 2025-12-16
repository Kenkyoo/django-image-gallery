import requests
from django.shortcuts import render

API_KEY = "_Lo9ruec1rqQ_-ERrp_NHgqbfBdANyAzPYaSLwGdXh0"
BASE_URL = "https://api.unsplash.com"


def index(request):
    return render(request, "core/hero.html")


def photos(request):
    data = None
    error_message = None
    q = request.POST.get("query") if request.method == "POST" else None

    try:
        if q:
            # Búsqueda por palabra clave
            API_URL = (
                f"{BASE_URL}/search/photos?query={q}&client_id={API_KEY}&per_page=24"
            )
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            # IMPORTANTE: En búsqueda, las fotos están en la clave ['results']
            data = response.json().get("results")
        else:
            # Fotos recientes (si no hay búsqueda)
            API_URL = f"{BASE_URL}/photos?client_id={API_KEY}&per_page=12"
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            # Aquí la API devuelve una lista directa
            data = response.json()

    except requests.exceptions.RequestException as e:
        error_message = f"Error al conectar con Unsplash: {e}"

    return render(
        request, "core/photos.html", {"data": data, "error": error_message, "query": q}
    )


def photo(request, photo_id):
    api_url = f"{BASE_URL}/photos/{photo_id}?client_id={API_KEY}"
    data = None
    error = None

    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        error = f"No se pudo obtener el detalle de la imagen: {e}"

    return render(request, "core/photo.html", {"data": data, "error": error})
