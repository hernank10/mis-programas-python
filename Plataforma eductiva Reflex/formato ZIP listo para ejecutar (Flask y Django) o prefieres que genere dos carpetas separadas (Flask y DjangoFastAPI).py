# Creating scaffold project with Flask, Django, FastAPI, Bootstrap components, gamification module, and 100 bilingual lessons.
import os, json, zipfile, textwrap, pathlib

BASE = "/mnt/data/rflex_scaffold"
os.makedirs(BASE, exist_ok=True)

def write(path, content, mode="w"):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, mode, encoding="utf-8") as f:
        f.write(content)

# 1) README
readme = textwrap.dedent("""\
    RFlex Scaffold - Flask + Django + FastAPI + Bootstrap
    ----------------------------------------------------
    Contenido:
    - flask_app/: prototipo Flask minimal
    - django_app/: scaffold Django + DRF minimal
    - fastapi_app/: scaffold FastAPI minimal
    - lessons_data/lessons.json: 100 lecciones bilingües (ES/EN)
    - scripts/import_lessons.py: script de ejemplo para importar lecciones
    - README.md (este archivo)
    
    Instrucciones rápidas:
    - Flask: ejecutar flask_app/README.md
    - Django: ver django_app/README.md
    - FastAPI: ver fastapi_app/README.md
    """)
write("README.md", readme)

# 2) Create Flask app minimal
flask_readme = textwrap.dedent("""\
    Flask prototype - Quick start
    ----------------------------
    1. Create virtualenv and install:
       python -m venv .venv
       source .venv/bin/activate
       pip install Flask
    2. Run:
       export FLASK_APP=app.py
       flask run
    """)
write("flask_app/README.md", flask_readme)

flask_app_py = textwrap.dedent("""\
    from flask import Flask, render_template, jsonify
    import json, os
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/api/lessons')
    def lessons_api():
        p = os.path.join(os.path.dirname(__file__), 'data', 'lessons.json')
        with open(p, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    
    if __name__ == '__main__':
        app.run(debug=True)
    """)
write("flask_app/app.py", flask_app_py)

flask_index = textwrap.dedent("""\
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
      <title>RFlex - Flask Prototype</title>
    </head>
    <body class="p-4">
      <div class="container">
        <h1>RFlex - Flask Prototype</h1>
        <div id="lessons" class="row"></div>
      </div>
      <script>
        fetch('/api/lessons').then(r=>r.json()).then(data=>{
          const el = document.getElementById('lessons');
          data.slice(0,12).forEach(l=>{
            const card = document.createElement('div');
            card.className='col-md-4';
            card.innerHTML = `<div class="card mb-3 p-3"><h5>${l.title_es} / ${l.title_en}</h5><p>${l.excerpt}</p></div>`;
            el.appendChild(card);
          });
        });
      </script>
    </body>
    </html>
    """)
write("flask_app/templates/index.html", flask_index)

# copy bootstrap placeholder static folder
write("flask_app/static/.gitkeep", "")

# copy lessons data placeholder (will fill later)
os.makedirs(os.path.join(BASE, "flask_app", "data"), exist_ok=True)

# 3) Django scaffold minimal files
django_readme = textwrap.dedent("""\
    Django scaffold - Quick start
    -----------------------------
    1. Create virtualenv and install:
       python -m venv .venv
       source .venv/bin/activate
       pip install Django djangorestframework
    
    2. Create superuser and run server:
       python manage.py migrate
       python manage.py createsuperuser
       python manage.py runserver
    """)
write("django_app/README.md", django_readme)

# manage.py
manage_py = textwrap.dedent("""\
    # manage.py placeholder - run Django project according to its docs
    print('Use real Django project in production. This scaffold contains example apps.')
    """)
write("django_app/manage.py", manage_py)

# Example Django app files: models, serializers, views, urls
write("django_app/lessons/models.py", textwrap.dedent("""\
    from django.db import models
    class Lesson(models.Model):
        title_es = models.CharField(max_length=255)
        title_en = models.CharField(max_length=255)
        content_es = models.TextField()
        content_en = models.TextField()
        excerpt = models.CharField(max_length=255, blank=True)
        level = models.CharField(max_length=10, default='A1')
        def __str__(self): return f\"{self.title_es} / {self.title_en}\"
    """))

write("django_app/lessons/serializers.py", textwrap.dedent("""\
    from rest_framework import serializers
    from .models import Lesson
    class LessonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Lesson
            fields = '__all__'
    """))

write("django_app/lessons/views.py", textwrap.dedent("""\
    from rest_framework import viewsets
    from .models import Lesson
    from .serializers import LessonSerializer
    class LessonViewSet(viewsets.ModelViewSet):
        queryset = Lesson.objects.all()
        serializer_class = LessonSerializer
    """))

write("django_app/lessons/urls.py", textwrap.dedent("""\
    from django.urls import path, include
    from rest_framework import routers
    from .views import LessonViewSet
    router = routers.DefaultRouter()
    router.register(r'lessons', LessonViewSet)
    urlpatterns = [path('api/', include(router.urls))]
    """))

# 4) FastAPI scaffold
fastapi_readme = textwrap.dedent("""\
    FastAPI scaffold - Quick start
    ------------------------------
    1. Create virtualenv and install:
       pip install fastapi uvicorn sqlmodel
    2. Run:
       uvicorn app.main:app --reload
    """)
write("fastapi_app/README.md", fastapi_readme)

fastapi_main = textwrap.dedent("""\
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from app.routers import lessons
    app = FastAPI(title='RFlex API (FastAPI)')
    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
    app.include_router(lessons.router, prefix='/lessons', tags=['lessons'])
    @app.get('/')
    def root():
        return {'message':'RFlex FastAPI scaffold'}
    """)
write("fastapi_app/app/main.py", fastapi_main)

fastapi_router = textwrap.dedent("""\
    from fastapi import APIRouter, HTTPException
    from typing import List
    import json, os
    router = APIRouter()
    @router.get('/', response_model=List[dict])
    def list_lessons():
        p = os.path.join(os.path.dirname(__file__), '..', 'data', 'lessons.json')
        p = os.path.normpath(p)
        with open(p, 'r', encoding='utf-8') as f:
            return json.load(f)
    """)
write("fastapi_app/app/routers/lessons.py", fastapi_router)
os.makedirs(os.path.join(BASE, "fastapi_app", "app", "data"), exist_ok=True)

# 5) Scripts and import tools
import_script = textwrap.dedent("""\
    # import_lessons.py - example to copy lessons JSON into DB (pseudo-code)
    import json, os
    p = os.path.join(os.path.dirname(__file__), 'lessons_data', 'lessons.json')
    with open(p, 'r', encoding='utf-8') as f:
        lessons = json.load(f)
    print(f'Lecciones cargadas: {len(lessons)}')
    # Implement DB insertion according to your stack (Django ORM / SQLModel / SQLAlchemy)
    """)
write("scripts/import_lessons.py", import_script)

# 6) Gamification module (simple implementation)
gamification = textwrap.dedent("""\
    # gamification service pseudo-code
    class GamificationService:
        def __init__(self, user_profile):
            self.user = user_profile
        def submit_attempt(self, lesson_id, score):
            # add points, update streak, award badges
            self.user['points'] = self.user.get('points', 0) + score
            if score > 80:
                self.user.setdefault('badges', []).append('lesson_master')
            return self.user
    """)
write("common/gamification.py", gamification)

# 7) Generate 100 bilingual lessons
lessons = []
for i in range(1, 101):
    lesson = {
        "id": i,
        "title_es": f"Lección {i:03d}: Regla ejemplo {i} (ES)",
        "title_en": f"Lesson {i:03d}: Example rule {i} (EN)",
        "content_es": f"Contenido de la lección {i} en español. Explicación de la regla morfosintáctica número {i}. Ejemplos y ejercicios.",
        "content_en": f"Lesson {i} content in English. Explanation of morphosyntactic rule number {i}. Examples and exercises.",
        "excerpt": f"Resumen breve de la lección {i}.",
        "level": "A1" if i<=33 else ("B1" if i<=66 else "C1")
    }
    lessons.append(lesson)

# write lessons in three locations (flask, fastapi, central folder)
write("lessons_data/lessons.json", json.dumps(lessons, ensure_ascii=False, indent=2))
write("flask_app/data/lessons.json", json.dumps(lessons, ensure_ascii=False, indent=2))
write("fastapi_app/app/data/lessons.json", json.dumps(lessons, ensure_ascii=False, indent=2))
write("django_app/lessons/initial_lessons.json", json.dumps(lessons, ensure_ascii=False, indent=2))

# 8) Create a simple Bootstrap poster image placeholder note
poster_note = "Poster created separately and available as A_educational_infographic_in_Spanish_titled_Migra.png in the /mnt/data folder."
write("POSTER_NOTE.txt", poster_note)

# 9) Create zip of the scaffold
zip_path = "/mnt/data/rflex_scaffold.zip"
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BASE):
        for fn in files:
            full = os.path.join(root, fn)
            arc = os.path.relpath(full, BASE)
            zf.write(full, arc)

zip_path

