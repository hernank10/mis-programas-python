#pip install spacy
#python -m spacy download es_core_news_sm
import spacy

# Cargar el modelo preentrenado de spaCy para el español
nlp = spacy.load('es_core_news_sm')

# Texto para analizar
oracion = "El gato negro corría rápidamente por el jardín mientras observaba a los pájaros."

# Procesar la oración
doc = nlp(oracion)

# Mostrar el análisis morfológico de cada palabra
print(f"{'Palabra':<15}{'Lema':<15}{'Categoría':<15}{'Detalles'}")
print("=" * 60)
for token in doc:
    print(f"{token.text:<15}{token.lemma_:<15}{token.pos_:<15}{token.tag_}")


