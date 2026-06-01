# Create educa_reflex_v6_django package with Reflex frontend + Django backend (history & peer review)
import os, textwrap, zipfile, shutil, stat, json

root = "/mnt/data/educa_reflex_v6_django"
if os.path.exists(root):
    shutil.rmtree(root)
os.makedirs(root, exist_ok=True)

def write(path, content):
    full = os.path.join(root, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# README
write("README.md", textwrap.dedent("""
Educa Reflex v6 Django - Demo package
Includes:
- Reflex frontend scaffold (login, dashboard, editable report, history and approve)
- Django backend (REST API) with models: User (via Django auth), Module, EditHistory, and approval workflow.
- Instructions to run locally with sqlite DB.

Run steps (UNIX-like):
1. Create venv:
   python3 -m venv .venv
   source .venv/bin/activate
2. Install:
   pip install -r requirements.txt
3. Apply migrations and seed data:
   cd backend_django
   python manage.py migrate
   python manage.py loaddata seed_initial.json
4. Run Django server:
   python manage.py runserver 0.0.0.0:8000
5. Run Reflex frontend (project root):
   reflex run
Frontend expects API at http://localhost:8000/api/
Login users seeded: teacher/teacherpass (is_staff=True), admin/adminpass (is_superuser), student/studentpass
"""))

# requirements
write("requirements.txt", "\n".join([
    "reflex",
    "Django>=4.2",
    "djangorestframework",
    "requests",
]))

# Reflex frontend - reuse earlier scaffold but point to Django API
write("edu_reflex/__init__.py", "# reflex package for Django demo\n")
write("edu_reflex/state.py", textwrap.dedent("""
import reflex as rx
import requests, os
API_BASE = os.getenv('API_BASE','http://localhost:8000/api')

class AuthState(rx.State):
    logged_in: bool = False
    role: str = ''
    username: str = ''

    def login(self, username, password):
        try:
            r = requests.post(f'{API_BASE}/auth/login/', json={'username': username, 'password': password})
            if r.status_code == 200:
                data = r.json()
                self.logged_in = True
                self.role = data.get('role','')
                self.username = username
                rx.redirect('/dashboard')
            else:
                rx.toast.error('Credenciales inválidas')
        except Exception:
            rx.toast.error('Error de conexión')

    def logout(self):
        try:
            requests.post(f'{API_BASE}/auth/logout/')
        finally:
            self.logged_in = False
            self.role = ''
            self.username = ''
            rx.redirect('/login')

class SyncState(rx.State):
    modules: list = []
    history: list = []
    sync_status: str = 'No sincronizado'

    def fetch_modules(self):
        try:
            r = requests.get(f'{API_BASE}/modules/')
            if r.status_code == 200:
                self.modules = r.json()
                self.sync_status = '✅ Sincronizado con Django API'
            else:
                self.sync_status = '⚠️ Error al sincronizar'
        except Exception:
            self.sync_status = '❌ No se pudo conectar'

    def send_updates(self):
        try:
            # bulk update via modules/update_many/
            r = requests.post(f'{API_BASE}/modules/update_many/', json=self.modules)
            if r.status_code == 200:
                self.sync_status = '✅ Actualización enviada'
            else:
                self.sync_status = '⚠️ Error al enviar'
        except Exception:
            self.sync_status = '❌ Error de conexión'

    def fetch_history(self):
        try:
            r = requests.get(f'{API_BASE}/history/')
            if r.status_code == 200:
                self.history = r.json()
        except Exception:
            self.history = []

    def approve(self, module_id):
        try:
            r = requests.post(f'{API_BASE}/modules/{module_id}/approve/')
            if r.status_code == 200:
                rx.toast.success('Aprobación registrada')
                self.fetch_modules()
            else:
                rx.toast.error('No autorizado o error')
        except Exception:
            rx.toast.error('Error de conexión')
"""))

write("edu_reflex/components/login_form.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.state import AuthState
def login_form():
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading('🔐 Acceso'),
                rx.input(placeholder='Usuario', id='username'),
                rx.input(placeholder='Contraseña', id='password', type='password'),
                rx.hstack(
                    rx.button('Ingresar', on_click=lambda: AuthState.login(rx.get_value('username'), rx.get_value('password'))),
                    rx.link('Volver', href='/')
                )
            ),
            padding='6', width='360px'
        )
    )
"""))

write("edu_reflex/components/report_table.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.state import SyncState, AuthState
import os, requests

API_BASE = os.getenv('API_BASE','http://localhost:8000/api')

def report_table():
    if not AuthState.logged_in or AuthState.role not in ['teacher','admin']:
        return rx.center(rx.text('Acceso restringido. Solo profesores o administradores.'))

    rows = []
    for m in SyncState.modules:
        mid = m.get('id')
        status_id = f'status_{mid}'
        reco_id = f'reco_{mid}'
        rows.append(
            rx.hstack(
                rx.box(rx.text(m.get('name')), width='30%'),
                rx.input(default_value=m.get('status'), id=status_id),
                rx.input(default_value=m.get('recommendations'), id=reco_id),
                rx.button('💾 Guardar', on_click=lambda _evt, mid=mid, sid=status_id, rid=reco_id: save_module(mid, sid, rid)),
                rx.button('✅ Aprobar', on_click=lambda _evt, mid=mid: approve_module(mid))
            , spacing='3', padding='2', border='1px solid #eee')
        )
    return rx.vstack(
        rx.heading('📊 Informe Técnico Editable (Django API)'),
        rx.text(SyncState.sync_status),
        rx.hstack(rx.button('Recargar desde servidor', on_click=SyncState.fetch_modules),
                 rx.button('Ver Historial', on_click=SyncState.fetch_history)),
        rx.vstack(*rows)
    )

def save_module(module_id, status_id, reco_id):
    status = rx.get_value(status_id)
    reco = rx.get_value(reco_id)
    try:
        r = requests.put(f'{API_BASE}/modules/{module_id}/', json={'status': status, 'recommendations': reco}, cookies=None)
        if r.status_code == 200:
            rx.toast.success('Guardado correctamente')
            SyncState.fetch_modules()
            SyncState.fetch_history()
        else:
            rx.toast.error('Error guardando (permiso?)')
    except Exception as e:
        rx.toast.error('Error de conexión al guardar')
        print(e)

def approve_module(module_id):
    SyncState.approve(module_id)
"""))

write("edu_reflex/components/history.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.state import SyncState, AuthState

def history_panel():
    if not AuthState.logged_in or AuthState.role not in ['teacher','admin']:
        return rx.center(rx.text('Acceso restringido.'))
    return rx.card(
        rx.vstack(
            rx.heading('🕘 Historial de Ediciones'),
            rx.foreach(SyncState.history, lambda h: rx.box(
                rx.text(f\"Módulo ID: {h.get('module_id')} | Campo: {h.get('field')}\") ,
                rx.text(f\"De: {h.get('old_value')} → A: {h.get('new_value')}\") ,
                rx.text(f\"Por usuario_id: {h.get('user_id')} a las {h.get('timestamp')}\") ,
                padding='2', border='1px solid #ddd'
            ))
        ),
        padding='4'
    )
"""))

write("edu_reflex/pages/index.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.components.login_form import login_form
def index_page():
    return rx.center(rx.vstack(rx.heading('Plataforma Educativa Reflex - Django Demo v6'), rx.link('Iniciar sesión', href='/login'), rx.link('Dashboard', href='/dashboard')))
"""))

write("edu_reflex/pages/login.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.components.login_form import login_form
def login_page():
    return login_form()
"""))

write("edu_reflex/pages/dashboard.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.components.sync_status import sync_status_panel
from edu_reflex.components.report_table import report_table
from edu_reflex.components.history import history_panel
from edu_reflex.state import AuthState

def dashboard_page():
    return rx.center(
        rx.vstack(
            rx.heading(f'Bienvenido {AuthState.username if AuthState.username else \"(invitado)\"}'),
            rx.hstack(rx.button('Cerrar sesión', on_click=AuthState.logout)),
            rx.divider(),
            report_table(),
            rx.divider(),
            history_panel()
        ),
        padding='4'
    )
"""))

write("edu_reflex/components/sync_status.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.state import SyncState

def sync_status_panel():
    return rx.card(
        rx.vstack(
            rx.heading('🔗 Sincronización Institucional (Django API)'),
            rx.text(SyncState.sync_status),
            rx.hstack(
                rx.button('Obtener datos', on_click=SyncState.fetch_modules),
                rx.button('Enviar cambios', on_click=SyncState.send_updates),
            ),
            rx.divider(),
            rx.foreach(SyncState.modules, lambda m: rx.box(rx.text(f\"{m.get('name')}: {m.get('status')}\"), padding='2', border='1px solid #ddd'))
        ),
        padding='4'
    )
"""))

write("app.py", textwrap.dedent("""
import reflex as rx
from edu_reflex.pages import index, login, dashboard
from edu_reflex.state import AuthState, SyncState

app = rx.App(state=AuthState)
app.add_page(index.index_page, route='/')
app.add_page(login.login_page, route='/login')
app.add_page(dashboard.dashboard_page, route='/dashboard')
app.compile()
"""))

# ---------------- Django backend ----------------
# manage.py
write("backend_django/manage.py", textwrap.dedent("""
#!/usr/bin/env python
import os, sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    execute_from_command_line(sys.argv)
"""))

# settings.py minimal
write("backend_django/backend_django/settings.py", textwrap.dedent("""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-dev-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
ROOT_URLCONF = 'backend_django.urls'
TEMPLATES = []
WSGI_APPLICATION = 'backend_django.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
STATIC_URL = '/static/'
"""))

write("backend_django/backend_django/urls.py", textwrap.dedent("""
from django.urls import path, include
urlpatterns = [
    path('api/', include('api.urls')),
]
"""))

write("backend_django/backend_django/wsgi.py", textwrap.dedent("""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')
application = get_wsgi_application()
"""))

# api app: models, serializers, views, urls, admin, migrations handled by user
write("backend_django/api/__init__.py", "")
write("backend_django/api/apps.py", textwrap.dedent("""
from django.apps import AppConfig
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
"""))

write("backend_django/api/models.py", textwrap.dedent("""
from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_modules')
    updated_at = models.DateTimeField(null=True, blank=True)
    approved_by_1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved1')
    approved_by_2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved2')
    final_approved = models.BooleanField(default=False)

class EditHistory(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    field = models.CharField(max_length=100)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
"""))

write("backend_django/api/serializers.py", textwrap.dedent("""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Module, EditHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','is_staff','is_superuser']

class ModuleSerializer(serializers.ModelSerializer):
    updated_by = UserSerializer(read_only=True)
    approved_by_1 = UserSerializer(read_only=True)
    approved_by_2 = UserSerializer(read_only=True)
    class Meta:
        model = Module
        fields = '__all__'

class EditHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = EditHistory
        fields = '__all__'
"""))

write("backend_django/api/views.py", textwrap.dedent("""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Module, EditHistory
from .serializers import ModuleSerializer, EditHistorySerializer, UserSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message':'ok', 'role': 'teacher' if user.is_staff else 'student'})
    return Response({'error':'invalid'}, status=401)

@api_view(['POST'])
def api_logout(request):
    logout(request)
    return Response({'message':'logged out'})

@api_view(['GET'])
def modules_list(request):
    modules = Module.objects.all().order_by('id')
    return Response(ModuleSerializer(modules, many=True).data)

@api_view(['PUT'])
def module_update(request, pk):
    if not request.user.is_authenticated or not request.user.is_staff:
        return Response({'error':'forbidden'}, status=403)
    m = get_object_or_404(Module, pk=pk)
    data = request.data
    # record history if changed
    if 'status' in data and data['status'] != m.status:
        EditHistory.objects.create(module=m, user=request.user, field='status', old_value=m.status, new_value=data['status'])
        m.status = data['status']
    if 'recommendations' in data and data['recommendations'] != m.recommendations:
        EditHistory.objects.create(module=m, user=request.user, field='recommendations', old_value=m.recommendations, new_value=data['recommendations'])
        m.recommendations = data['recommendations']
    m.updated_by = request.user
    m.updated_at = timezone.now()
    m.save()
    return Response({'message':'updated'})

@api_view(['POST'])
def module_approve(request, pk):
    if not request.user.is_authenticated or not request.user.is_staff:
        return Response({'error':'forbidden'}, status=403)
    m = get_object_or_404(Module, pk=pk)
    if m.approved_by_1 == request.user or m.approved_by_2 == request.user:
        return Response({'message':'already approved'})
    if not m.approved_by_1:
        m.approved_by_1 = request.user
    elif not m.approved_by_2:
        m.approved_by_2 = request.user
    if m.approved_by_1 and m.approved_by_2:
        m.final_approved = True
    m.save()
    return Response({'message':'approved', 'final_approved': m.final_approved})

@api_view(['GET'])
def history_list(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return Response({'error':'forbidden'}, status=403)
    history = EditHistory.objects.all().order_by('-timestamp')[:200]
    return Response(EditHistorySerializer(history, many=True).data)
"""))

write("backend_django/api/urls.py", textwrap.dedent("""
from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.api_login),
    path('auth/logout/', views.api_logout),
    path('modules/', views.modules_list),
    path('modules/<int:pk>/', views.module_update),
    path('modules/<int:pk>/approve/', views.module_approve),
    path('modules/update_many/', views.module_update),  # reuse update for simplicity
    path('history/', views.history_list),
]
"""))

# seed fixture
seed = {
  "model": "api.module",
  "pk": 1,
  "fields": {}
}
# create a simple fixture JSON with users and modules via loaddata simpler: create seed_initial.json with Module entries only
seed_modules = [
  {"model":"api.module","pk":1,"fields":{"name":"Auth (Usuarios y Roles)","description":"Registro y roles","status":"Implementado","recommendations":"Agregar recuperación de contraseña"}},
  {"model":"api.module","pk":2,"fields":{"name":"Ejercicios Interactivos","description":"100 ejercicios bilingües","status":"Implementado","recommendations":"Mejorar UI"}},
  {"model":"api.module","pk":3,"fields":{"name":"Gamificación","description":"Puntos y medallas","status":"Implementado","recommendations":"Añadir insignias animadas"}},
  {"model":"api.module","pk":4,"fields":{"name":"Noticias y Muro","description":"Noticias y publicaciones","status":"Parcial","recommendations":"Panel de creación de posts"}},
  {"model":"api.module","pk":5,"fields":{"name":"Clases en Vivo","description":"Calendario y enlaces","status":"Pendiente","recommendations":"Integrar Jitsi"}},
]
write("backend_django/seed_initial.json", json.dumps(seed_modules, indent=2))

# top-level packaging complete; create zip
zip_path = "/mnt/data/educa_reflex_v6_django.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for base, dirs, files in os.walk(root):
        for f in files:
            full = os.path.join(base, f)
            arcname = os.path.relpath(full, root)
            zf.write(full, arcname)

zip_path

