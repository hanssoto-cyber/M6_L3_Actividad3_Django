from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm
from .models import Contacto


# MTV: View contiene la lógica de negocio y procesa las solicitudes del usuario.

def home(request):
    """Vista principal - muestra la página de inicio con información dinámica."""
    tecnologias = ['Python', 'Django', 'HTML5', 'CSS3', 'Bootstrap 5', 'SQLite']
    caracteristicas = [
        {'icono': '🔒', 'titulo': 'Seguro', 'descripcion': 'Protección integrada contra CSRF, XSS y SQL Injection.'},
        {'icono': '⚡', 'titulo': 'Rápido', 'descripcion': 'ORM optimizado y sistema de caché incorporado.'},
        {'icono': '♻️', 'titulo': 'DRY', 'descripcion': 'No te repitas. Reutiliza componentes y lógica fácilmente.'},
        {'icono': '🧩', 'titulo': 'Modular', 'descripcion': 'Arquitectura MTV que separa modelo, template y vista.'},
    ]
    context = {
        'titulo': 'Desarrollo de Aplicaciones Web con Django',
        'subtitulo': 'Aprende el patrón MTV, herencia de plantillas y formularios con validación backend.',
        'tecnologias': tecnologias,
        'caracteristicas': caracteristicas,
    }
    return render(request, 'home.html', context)


def sobre_django(request):
    """Vista informativa sobre Django y el patrón MTV."""
    temas = [
        {'titulo': 'Entorno Virtual', 'descripcion': 'Aísla las dependencias del proyecto con virtualenv o venv.'},
        {'titulo': 'Patrón MTV', 'descripcion': 'Model-Template-View: separa datos, presentación y lógica.'},
        {'titulo': 'Templates', 'descripcion': 'Sistema de plantillas con herencia, bloques y variables dinámicas.'},
        {'titulo': 'Formularios', 'descripcion': 'Validación en el backend con Django Forms y ModelForms.'},
        {'titulo': 'ORM Django', 'descripcion': 'Interactúa con la base de datos usando Python, sin SQL directo.'},
        {'titulo': 'Bootstrap 5', 'descripcion': 'Diseño responsivo con componentes predefinidos via CDN.'},
    ]
    context = {
        'titulo': 'Sobre Django',
        'temas': temas,
    }
    return render(request, 'sobre_django.html', context)


def contacto(request):
    """
    Vista de contacto con formulario.
    Valida los datos en el backend usando Django Forms.
    GET: Muestra el formulario vacío.
    POST: Procesa y valida los datos enviados.
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '✅ ¡Mensaje enviado correctamente! Nos pondremos en contacto contigo pronto.'
            )
            return redirect('contacto')
        else:
            messages.error(request, '❌ Por favor, corrige los errores del formulario.')
    else:
        form = ContactoForm()

    # Mostrar mensajes enviados (últimos 5) para demostrar el modelo
    mensajes_recibidos = Contacto.objects.all()[:5]

    context = {
        'titulo': 'Contacto',
        'form': form,
        'mensajes_recibidos': mensajes_recibidos,
    }
    return render(request, 'contacto.html', context)
