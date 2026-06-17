-- ============================================================
-- ESQUEMA LMS EDUCATIVO - mis-programas-python
-- ============================================================

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    rol TEXT DEFAULT 'estudiante',
    activo INTEGER DEFAULT 1
);

-- Tabla de niveles (A1-C2)
CREATE TABLE IF NOT EXISTS niveles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    orden INTEGER DEFAULT 0
);

-- Tabla de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    descripcion TEXT,
    nivel_id INTEGER,
    duracion_horas INTEGER DEFAULT 0,
    activo INTEGER DEFAULT 1,
    FOREIGN KEY (nivel_id) REFERENCES niveles(id)
);

-- Tabla de lecciones
CREATE TABLE IF NOT EXISTS lecciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    curso_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    tipo TEXT DEFAULT 'teoria',
    contenido_html TEXT,
    duracion_minutos INTEGER DEFAULT 30,
    puntos INTEGER DEFAULT 10,
    orden INTEGER DEFAULT 0,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Tabla de progreso
CREATE TABLE IF NOT EXISTS progreso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    leccion_id INTEGER,
    completado INTEGER DEFAULT 0,
    puntaje INTEGER DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (leccion_id) REFERENCES lecciones(id)
);

-- Tabla de declinaciones latinas
CREATE TABLE IF NOT EXISTS declinaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT NOT NULL,
    declinacion INTEGER NOT NULL,
    genero TEXT,
    traduccion TEXT,
    nominativo TEXT,
    genitivo TEXT,
    dativo TEXT,
    acusativo TEXT,
    ablativo TEXT
);

-- Tabla de ejercicios de inglés
CREATE TABLE IF NOT EXISTS ejercicios_ingles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT NOT NULL,
    pregunta TEXT NOT NULL,
    respuesta_correcta TEXT NOT NULL,
    explicacion TEXT
);

-- ============================================================
-- DATOS INICIALES
-- ============================================================

-- Niveles
INSERT OR IGNORE INTO niveles (codigo, nombre, orden) VALUES
('A1', 'Principiante', 1),
('A2', 'Básico', 2),
('B1', 'Intermedio', 3),
('B2', 'Intermedio Alto', 4),
('C1', 'Avanzado', 5),
('C2', 'Maestría', 6);

-- Usuarios
INSERT OR IGNORE INTO usuarios (username, password, email, rol) VALUES
('admin', 'admin123', 'admin@ejemplo.com', 'admin'),
('estudiante', 'estudiante123', 'estudiante@ejemplo.com', 'estudiante');

-- Cursos
INSERT OR IGNORE INTO cursos (titulo, slug, descripcion, nivel_id, duracion_horas) VALUES
('Español A1 - Principiantes', 'espanol-a1', 'Aprende español desde cero.', 1, 40),
('Latín - Declinaciones', 'latin-declinaciones', 'Aprende las declinaciones latinas.', NULL, 30);

-- Declinaciones latinas
INSERT OR IGNORE INTO declinaciones (palabra, declinacion, genero, traduccion, nominativo, genitivo, dativo, acusativo, ablativo) VALUES
('rosa', 1, 'femenino', 'rosa', 'rosa', 'rosae', 'rosae', 'rosam', 'rosā'),
('puella', 1, 'femenino', 'niña', 'puella', 'puellae', 'puellae', 'puellam', 'puellā'),
('servus', 2, 'masculino', 'esclavo', 'servus', 'servi', 'servo', 'servum', 'servo');

-- Ejercicios de inglés
INSERT OR IGNORE INTO ejercicios_ingles (categoria, pregunta, respuesta_correcta, explicacion) VALUES
('plurales', '¿Cuál es el plural de "cat"?', 'cats', 'Los plurales regulares añaden -s'),
('verbos', '¿Cuál es el pasado de "go"?', 'went', 'Verbo irregular'),
('vocabulario', '¿Cómo se dice "casa" en inglés?', 'house', 'Lugar donde se vive');

SELECT '✅ Base de datos creada' as mensaje;
