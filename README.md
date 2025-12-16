📸 Django Image Gallery (Unsplash API)

Una aplicación web desarrollada con Django que consume la API de Unsplash para explorar y buscar fotografías de alta resolución. El proyecto permite visualizar una galería dinámica y acceder a detalles específicos de cada imagen.

🚀 Link del Deploy: django-image-gallery-aa64.onrender.com

✨ Características Principales

Galería Dinámica: Visualización de fotos recientes o resultados de búsqueda directamente desde Unsplash.

Buscador Funcional: Filtrado de imágenes por palabras clave (query) mediante un formulario (método POST).

Detalle de Foto: Página dedicada para cada imagen, accesible a través de su ID, mostrando metadatos avanzados (autor, likes, ubicación, datos EXIF).

Manejo de Errores: Implementación de bloques try/except para gestionar fallos en la conexión y errores HTTP (404, 500), garantizando una experiencia de usuario robusta.

Diseño Responsive: Interfaz construida con Bootstrap 5 para una visualización óptima en cualquier dispositivo.

🛠️ Tecnologías utilizadas

El proyecto está construido sobre un stack moderno y escalable:

Tecnología

Rol

Django 5.x

Framework Backend principal

Python 3.x

Lenguaje de programación

Requests

Cliente HTTP para consumir la API externa

Bootstrap 5

Estilizado y componentes frontend

Unsplash API

Fuente de datos para las imágenes

Render

Servicio de despliegue continuo (Deployment)

⚙️ Estructura de Rutas y Navegación

El proyecto expone los siguientes endpoints:

URL Pattern

Vista (View)

Descripción

/

views.index

Página principal de bienvenida (Hero).

/photos/

views.photos

Galería principal (soporta GET y POST para la búsqueda).

/photos/<str:photo_id>/

views.photo

Detalle individual de la fotografía, el ID es capturado de la URL.

🔎 Manejo de Parámetros y API Calls

El corazón del proyecto reside en dos vistas clave:

1. Galería y Búsqueda (views.photos)

Esta vista utiliza lógica condicional para determinar qué URL de API llamar:

def photos(request):
    # ... (omitiendo try/except por brevedad)

    if q:
        # Petición a la API de BÚSQUEDA
        API_URL = f"{BASE_URL}/search/photos?query={q}&client_id={API_KEY}"
        data = response.json().get('results') 
    else:
        # Petición a la API de FOTOS RECIENTES
        API_URL = f"{BASE_URL}/photos?client_id={API_KEY}"
        data = response.json()


2. Detalle de Imagen (views.photo)

La URL de Django está configurada para recibir el ID alfanumérico como una cadena (<str:photo_id>), lo cual permite construir la URL de la API de forma dinámica y exacta:

# urls.py
path("photos/<str:photo_id>/", views.photo, name="photo"),

# views.py
def photo(request, photo_id):
    # El ID capturado se inyecta en la URL
    api_url = f"{BASE_URL}/photos/{photo_id}?client_id={API_KEY}"
    # ... hace la petición y renderiza el template


🚀 Instalación Local

Sigue estos pasos para poner en marcha el proyecto:

Clona el repositorio:

git clone [https://github.com/Kenkyoo/django-image-gallery.git](https://github.com/Kenkyoo/django-image-gallery.git)
cd django-image-gallery


Crea un entorno virtual e instálalo:

python -m venv venv
source venv/bin/activate  # Mac/Linux
# o venv\Scripts\activate  # Windows
pip install -r requirements.txt


Configura tu API Key:
Asegúrate de que la variable API_KEY en views.py contenga tu clave de acceso de Unsplash.

Ejecuta el servidor de desarrollo:

python manage.py runserver


Abre http://127.0.0.1:8000 en tu navegador.

👨‍💻 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, no dudes en abrir un issue o enviar un pull request.

Autor: Kenkyoo