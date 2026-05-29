# M6 L3 - Desarrollo de Aplicación Web con Django

## Cómo ejecutar el proyecto

```bash
# 1. Activar entorno virtual
# Windows:
env\Scripts\activate

# 2. Ejecutar migraciones (si no se han ejecutado)
python manage.py migrate

# 3. Iniciar servidor de desarrollo
python manage.py runserver

# 4. Abrir en el navegador
http://127.0.0.1:8000
```

---

## Páginas disponibles

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | `home` | Página principal con Hero, características, stack tecnológico y patrón MTV |
| `/sobre-django/` | `sobre_django` | Comparación MVC vs MTV, temas del módulo, herencia de plantillas |
| `/contacto/` | `contacto` | Formulario con validación backend Django |
| `/admin/` | Django Admin | Panel de administración (crear superusuario con `createsuperuser`) |

---

## Herencia de Plantillas

```
base.html               ← Contiene: <html>, navbar, footer, messages, Bootstrap CDN
    ├── home.html       ← {% extends "base.html" %} + {% block contenido %}
    ├── sobre_django.html
    └── contacto.html
```

## Patrón MTV en acción

- **Model** (`models.py`): `Contacto` con campos nombre, email, asunto, mensaje
- **Template** (`templates/*.html`): HTML con `{{ variables }}` y `{% tags %}`
- **View** (`views.py`): procesa GET/POST, valida formulario, retorna `render()`

## Validación del formulario (Backend)

En `forms.py`:
- `clean_nombre()`: valida que solo contenga letras y tenga ≥2 caracteres
- `clean_mensaje()`: valida mínimo 10 caracteres
- Validación de email: manejada automáticamente por Django `EmailField`

En `views.py`:
- `form.is_valid()` ejecuta todas las validaciones
- Si pasa: `form.save()` guarda en BD y redirige (PRG pattern)
- Si falla: renderiza el formulario con los errores mostrados
