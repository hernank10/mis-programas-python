import sqlite3
import re
from collections import defaultdict

class VerbAnalyzer:
    def __init__(self):
        self.suffix_rules = {
            'ar': {'type': 'regular', 'category': 'first'},
            'er': {'type': 'regular', 'category': 'second'},
            'ir': {'type': 'regular', 'category': 'third'}
        }
        self.irregular_verbs = self.load_irregular_verbs()
        
    def analyze(self, verb):
        if verb in self.irregular_verbs:
            return self.irregular_verbs[verb]
        
        for suffix, info in self.suffix_rules.items():
            if verb.endswith(suffix):
                return {
                    'base': verb[:-len(suffix)],
                    'suffix': suffix,
                    'type': info['type'],
                    'category': info['category']
                }
        return {'error': 'Verbo no reconocido'}

    def load_irregular_verbs(self):
        return {
            'tener': {'base': 'ten', 'type': 'irregular', 'changes': 'e→ie'},
            'hacer': {'base': 'hac', 'type': 'irregular', 'changes': 'c→z'},
            'ser': {'base': 's', 'type': 'irregular', 'changes': 'altamente irregular'}
        }

class SpanishSoundex:
    def __init__(self):
        self.mapping = {
            'B': '1', 'F': '1', 'P': '1', 'V': '1',
            'C': '2', 'S': '2', 'Z': '2', 'K': '2', 'Q': '2',
            'D': '3', 'T': '3',
            'L': '4', 'LL': '4',
            'M': '5', 'N': '5', 'Ñ': '5',
            'G': '6', 'J': '6', 'X': '6',
            'R': '7', 'RR': '7'
        }
    
    def encode(self, word):
        word = word.upper().replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        if not word:
            return ''
        
        first_char = word[0]
        code = [first_char]
        previous = self.get_mapped_char(first_char)
        
        for char in word[1:]:
            current = self.get_mapped_char(char)
            if current and current != previous:
                code.append(current)
                previous = current
        
        code = self._normalize_code(''.join(code))
        return code
    
    def get_mapped_char(self, char):
        if char in ['A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y']:
            return None
        for k, v in self.mapping.items():
            if char in k:
                return v
        return None
    
    def _normalize_code(self, code):
        code = code.replace('4', '').replace('7', '')  # Simplificación para español
        return (code + '000')[:4]

class Conjugator:
    PLANTILLAS = {
        'ar': {
            'presente': {
                'yo': 'o',
                'tú': 'as',
                'él': 'a',
                'nosotros': 'amos',
                'vosotros': 'áis',
                'ellos': 'an'
            }
        },
        'er': {
            'presente': {
                'yo': 'o',
                'tú': 'es',
                'él': 'e',
                'nosotros': 'emos',
                'vosotros': 'éis',
                'ellos': 'en'
            }
        },
        'ir': {
            'presente': {
                'yo': 'o',
                'tú': 'es',
                'él': 'e',
                'nosotros': 'imos',
                'vosotros': 'ís',
                'ellos': 'en'
            }
        }
    }
    
    IRREGULARES = {
        'tener': {
            'presente': {
                'yo': 'tengo',
                'tú': 'tienes',
                'él': 'tiene',
                'nosotros': 'tenemos',
                'vosotros': 'tenéis',
                'ellos': 'tienen'
            }
        }
    }
    
    def conjugate(self, verb):
        if verb in self.IRREGULARES:
            return self.IRREGULARES[verb]
        
        analyzer = VerbAnalyzer()
        analysis = analyzer.analyze(verb)
        if 'error' in analysis:
            return {'error': analysis['error']}
        
        suffix = analysis['suffix']
        root = analysis['base']
        return {
            tense: {person: root + ending 
                    for person, ending in persons.items()}
            for tense, persons in self.PLANTILLAS[suffix].items()
        }

class VerbDatabase:
    def __init__(self, db_name='verbs.db'):
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
    
    def _create_tables(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS verbs
                            (id INTEGER PRIMARY KEY,
                             verb TEXT UNIQUE,
                             base TEXT,
                             suffix TEXT,
                             type TEXT)''')
        
        self.conn.execute('''CREATE TABLE IF NOT EXISTS conjugations
                            (verb_id INTEGER,
                             tense TEXT,
                             person TEXT,
                             form TEXT,
                             FOREIGN KEY(verb_id) REFERENCES verbs(id))''')
    
    def save_verb(self, verb_data):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT OR REPLACE INTO verbs 
                        (verb, base, suffix, type)
                        VALUES (?, ?, ?, ?)''',
                     (verb_data['verb'], verb_data['base'],
                      verb_data['suffix'], verb_data['type']))
        verb_id = cursor.lastrowid
        
        conjugations = Conjugator().conjugate(verb_data['verb'])
        for tense, persons in conjugations.items():
            for person, form in persons.items():
                cursor.execute('''INSERT INTO conjugations
                                (verb_id, tense, person, form)
                                VALUES (?, ?, ?, ?)''',
                             (verb_id, tense, person, form))
        self.conn.commit()
    
    def search_soundex(self, word):
        soundex = SpanishSoundex().encode(word)
        cursor = self.conn.cursor()
        cursor.execute('''SELECT verb FROM verbs
                        WHERE soundex = ?''', (soundex,))
        return [row[0] for row in cursor.fetchall()]

class VerbCLI:
    def __init__(self):
        self.analyzer = VerbAnalyzer()
        self.conjugator = Conjugator()
        self.soundex = SpanishSoundex()
        self.db = VerbDatabase()
    
    def run(self):
        print("Sistema de Análisis Verbal Español")
        while True:
            command = input("\nComando (analizar/conjugar/buscar/agregar/salir): ").lower()
            
            if command == 'salir':
                break
                
            if command == 'analizar':
                verb = input("Verbo a analizar: ").lower()
                analysis = self.analyzer.analyze(verb)
                print("\nAnálisis:")
                for k, v in analysis.items():
                    print(f"{k.capitalize()}: {v}")
            
            elif command == 'conjugar':
                verb = input("Verbo a conjugar: ").lower()
                conjugations = self.conjugator.conjugate(verb)
                print("\nConjugaciones:")
                for tense, persons in conjugations.items():
                    print(f"\n{tense.capitalize()}:")
                    for person, form in persons.items():
                        print(f"{person}: {form}")
            
            elif command == 'buscar':
                word = input("Palabra para búsqueda fonética: ").lower()
                results = self.db.search_soundex(word)
                print(f"\nResultados para {word}:")
                print(", ".join(results) if results else "No se encontraron resultados")
            
            elif command == 'agregar':
                verb = input("Nuevo verbo: ").lower()
                analysis = self.analyzer.analyze(verb)
                if 'error' not in analysis:
                    self.db.save_verb({
                        'verb': verb,
                        'base': analysis['base'],
                        'suffix': analysis['suffix'],
                        'type': analysis['type']
                    })
                    print(f"Verbo {verb} agregado correctamente")
                else:
                    print("Error: Verbo no válido")
            
            else:
                print("Comando no reconocido")

if __name__ == '__main__':
    # Inicializar con datos de ejemplo
    db = VerbDatabase()
    for verb in ['amar', 'temer', 'partir', 'tener', 'hacer']:
        db.save_verb({'verb': verb, **VerbAnalyzer().analyze(verb)})
    
    cli = VerbCLI()
    cli.run()
