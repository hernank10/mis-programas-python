# -*- coding: utf-8 -*-
import random

# Datos de la tabla comparativa con 100+ ejemplos
TABLA_ORACIONES = [
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "She bought a new car.",
        "ejemplo_es": "Ella compró un coche nuevo."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where are you going?",
        "ejemplo_es": "¿A dónde vas?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Clean your room.",
        "ejemplo_es": "Limpia tu habitación."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a great idea!",
        "ejemplo_es": "¡Qué gran idea!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The sun is hot.",
        "ejemplo_es": "El sol está caliente."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Do you like coffee?",
        "ejemplo_es": "¿Te gusta el café?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't touch that!",
        "ejemplo_es": "¡No toques eso!"
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How fast he runs!",
        "ejemplo_es": "¡Qué rápido corre!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "My cat is sleeping.",
        "ejemplo_es": "Mi gato está durmiendo."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "When is the meeting?",
        "ejemplo_es": "¿Cuándo es la reunión?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Please be quiet.",
        "ejemplo_es": "Por favor, guarden silencio."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a perfect day!",
        "ejemplo_es": "¡Qué día tan perfecto!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "He speaks three languages.",
        "ejemplo_es": "Él habla tres idiomas."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Did you finish your homework?",
        "ejemplo_es": "¿Terminaste tu tarea?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Come here immediately!",
        "ejemplo_es": "¡Ven aquí inmediatamente!"
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How tall he is!",
        "ejemplo_es": "¡Qué alto es él!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The book is on the table.",
        "ejemplo_es": "El libro está en la mesa."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Who is at the door?",
        "ejemplo_es": "¿Quién está en la puerta?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't forget your keys.",
        "ejemplo_es": "No olvides tus llaves."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a relief!",
        "ejemplo_es": "¡Qué alivio!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I am learning a new skill.",
        "ejemplo_es": "Estoy aprendiendo una nueva habilidad."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Are you feeling better?",
        "ejemplo_es": "¿Te sientes mejor?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Go to bed now.",
        "ejemplo_es": "Ve a la cama ahora."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How wonderful this is!",
        "ejemplo_es": "¡Qué maravilloso es esto!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The movie starts at eight.",
        "ejemplo_es": "La película empieza a las ocho."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Why are you laughing?",
        "ejemplo_es": "¿Por qué te ríes?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't make so much noise.",
        "ejemplo_es": "No hagas tanto ruido."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a mess!",
        "ejemplo_es": "¡Qué desorden!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "We will travel to Paris next month.",
        "ejemplo_es": "Viajaremos a París el próximo mes."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Can you help me?",
        "ejemplo_es": "¿Puedes ayudarme?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Watch out!",
        "ejemplo_es": "¡Cuidado!"
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How cute she is!",
        "ejemplo_es": "¡Qué linda es ella!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "He is a good student.",
        "ejemplo_es": "Él es un buen estudiante."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Is this your book?",
        "ejemplo_es": "¿Este es tu libro?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't be afraid.",
        "ejemplo_es": "No tengas miedo."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a surprise!",
        "ejemplo_es": "¡Qué sorpresa!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The water is cold.",
        "ejemplo_es": "El agua está fría."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where did you find this?",
        "ejemplo_es": "¿Dónde encontraste esto?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Take a deep breath.",
        "ejemplo_es": "Respira hondo."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How delicious this cake is!",
        "ejemplo_es": "¡Qué delicioso es este pastel!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I need to buy some groceries.",
        "ejemplo_es": "Necesito comprar algunas provisiones."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Have you seen my keys?",
        "ejemplo_es": "¿Has visto mis llaves?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't give up.",
        "ejemplo_es": "No te rindas."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What an amazing view!",
        "ejemplo_es": "¡Qué vista tan increíble!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "They live in a small house.",
        "ejemplo_es": "Ellos viven en una casa pequeña."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Will it rain tomorrow?",
        "ejemplo_es": "¿Lloverá mañana?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Listen to me carefully.",
        "ejemplo_es": "Escúchame atentamente."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How kind of you!",
        "ejemplo_es": "¡Qué amable de tu parte!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "We are going to the beach.",
        "ejemplo_es": "Vamos a la playa."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where did you put my glasses?",
        "ejemplo_es": "¿Dónde pusiste mis gafas?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't be sad.",
        "ejemplo_es": "No estés triste."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a beautiful smile!",
        "ejemplo_es": "¡Qué sonrisa tan bonita!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "He walks to school every day.",
        "ejemplo_es": "Él camina a la escuela todos los días."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Could you please tell me the time?",
        "ejemplo_es": "¿Podrías decirme la hora, por favor?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Remember to call me.",
        "ejemplo_es": "Recuerda llamarme."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How strange this is!",
        "ejemplo_es": "¡Qué extraño es esto!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The train arrived late.",
        "ejemplo_es": "El tren llegó tarde."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Who ate the last cookie?",
        "ejemplo_es": "¿Quién se comió la última galleta?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Come and sit down.",
        "ejemplo_es": "Ven y siéntate."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a wonderful surprise!",
        "ejemplo_es": "¡Qué sorpresa tan maravillosa!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "She works as a teacher.",
        "ejemplo_es": "Ella trabaja como profesora."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Do you have any pets?",
        "ejemplo_es": "¿Tienes mascotas?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Drive carefully.",
        "ejemplo_es": "Conduce con cuidado."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How amazing!",
        "ejemplo_es": "¡Qué asombroso!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I love to listen to music.",
        "ejemplo_es": "Me encanta escuchar música."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "When did you last see him?",
        "ejemplo_es": "¿Cuándo fue la última vez que lo viste?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Please, give me your hand.",
        "ejemplo_es": "Por favor, dame tu mano."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a big house!",
        "ejemplo_es": "¡Qué casa tan grande!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "He is a great cook.",
        "ejemplo_es": "Él es un gran cocinero."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where were you last night?",
        "ejemplo_es": "¿Dónde estuviste anoche?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't speak so loudly.",
        "ejemplo_es": "No hables tan fuerte."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How funny!",
        "ejemplo_es": "¡Qué gracioso!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "We are a team.",
        "ejemplo_es": "Somos un equipo."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Are you a doctor?",
        "ejemplo_es": "¿Eres médico?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Be on time.",
        "ejemplo_es": "Sé puntual."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a beautiful voice!",
        "ejemplo_es": "¡Qué voz tan hermosa!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The weather is very hot.",
        "ejemplo_es": "El clima es muy caluroso."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "When will you be back?",
        "ejemplo_es": "¿Cuándo volverás?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Give me a hand.",
        "ejemplo_es": "Échame una mano."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How wonderful this concert is!",
        "ejemplo_es": "¡Qué maravilloso es este concierto!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "He is running in the park.",
        "ejemplo_es": "Él está corriendo en el parque."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Is it cold outside?",
        "ejemplo_es": "¿Hace frío afuera?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't forget to smile.",
        "ejemplo_es": "No olvides sonreír."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a fantastic show!",
        "ejemplo_es": "¡Qué espectáculo tan fantástico!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I need to go to the bank.",
        "ejemplo_es": "Necesito ir al banco."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Why is the sky blue?",
        "ejemplo_es": "¿Por qué el cielo es azul?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Wait for me.",
        "ejemplo_es": "Espérame."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How exciting!",
        "ejemplo_es": "¡Qué emocionante!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "They are building a new school.",
        "ejemplo_es": "Están construyendo una nueva escuela."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Did you see that?",
        "ejemplo_es": "¿Viste eso?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't be shy.",
        "ejemplo_es": "No seas tímido."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a tall building!",
        "ejemplo_es": "¡Qué edificio tan alto!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The test was difficult.",
        "ejemplo_es": "El examen fue difícil."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Are you going to the party?",
        "ejemplo_es": "¿Vas a la fiesta?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Please, pass me the salt.",
        "ejemplo_es": "Por favor, pásame la sal."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How quickly time passes!",
        "ejemplo_es": "¡Qué rápido pasa el tiempo!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The flowers are beautiful.",
        "ejemplo_es": "Las flores son hermosas."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "What do you want to eat?",
        "ejemplo_es": "¿Qué quieres comer?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Stop talking now.",
        "ejemplo_es": "Deja de hablar ahora."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a big dog!",
        "ejemplo_es": "¡Qué perro tan grande!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I went to the store yesterday.",
        "ejemplo_es": "Fui a la tienda ayer."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where is the bathroom?",
        "ejemplo_es": "¿Dónde está el baño?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't park here.",
        "ejemplo_es": "No te estaciones aquí."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How kind!",
        "ejemplo_es": "¡Qué amable!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The children are playing outside.",
        "ejemplo_es": "Los niños están jugando afuera."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Is the movie over?",
        "ejemplo_es": "¿Terminó la película?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Turn off the lights.",
        "ejemplo_es": "Apaga las luces."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What an incredible performance!",
        "ejemplo_es": "¡Qué actuación tan increíble!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I love my new computer.",
        "ejemplo_es": "Me encanta mi nuevo ordenador."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "How do you do that?",
        "ejemplo_es": "¿Cómo haces eso?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Open your book.",
        "ejemplo_es": "Abre tu libro."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How wonderful!",
        "ejemplo_es": "¡Qué maravilloso!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "She looks happy.",
        "ejemplo_es": "Ella se ve feliz."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Who is coming to dinner?",
        "ejemplo_es": "¿Quién viene a cenar?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't be late for the meeting.",
        "ejemplo_es": "No llegues tarde a la reunión."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a beautiful painting!",
        "ejemplo_es": "¡Qué pintura tan hermosa!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The cat is on the roof.",
        "ejemplo_es": "El gato está en el tejado."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Can you see the stars?",
        "ejemplo_es": "¿Puedes ver las estrellas?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Close your eyes.",
        "ejemplo_es": "Cierra los ojos."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How hot it is!",
        "ejemplo_es": "¡Qué calor hace!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I am so tired.",
        "ejemplo_es": "Estoy muy cansado."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Do you need help?",
        "ejemplo_es": "¿Necesitas ayuda?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Don't talk to strangers.",
        "ejemplo_es": "No hables con extraños."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a terrible storm!",
        "ejemplo_es": "¡Qué tormenta tan terrible!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The dog is wagging its tail.",
        "ejemplo_es": "El perro está moviendo la cola."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Where is the post office?",
        "ejemplo_es": "¿Dónde está la oficina de correos?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Please, have a seat.",
        "ejemplo_es": "Por favor, toma asiento."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How exciting this movie is!",
        "ejemplo_es": "¡Qué emocionante es esta película!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "The children are playing in the garden.",
        "ejemplo_es": "Los niños están jugando en el jardín."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "Is there a doctor in the house?",
        "ejemplo_es": "¿Hay un doctor en la casa?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Stop right there!",
        "ejemplo_es": "¡Detente ahí mismo!"
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "What a beautiful sunset!",
        "ejemplo_es": "¡Qué puesta de sol tan hermosa!"
    },
    {
        "tipo": "Declarativa",
        "regla": "Sujeto-Verbo-Objeto. Termina con un punto.",
        "ejemplo_en": "I am reading a book.",
        "ejemplo_es": "Estoy leyendo un libro."
    },
    {
        "tipo": "Interrogativa",
        "regla": "Comienza con una palabra interrogativa o un auxiliar. Termina con un signo de interrogación.",
        "ejemplo_en": "When do you wake up?",
        "ejemplo_es": "¿Cuándo te despiertas?"
    },
    {
        "tipo": "Imperativa",
        "regla": "Sin sujeto (implica 'you'). Termina con un punto o exclamación.",
        "ejemplo_en": "Call me later.",
        "ejemplo_es": "Llámame más tarde."
    },
    {
        "tipo": "Exclamativa",
        "regla": "Expresa emoción. Comienza con 'what' o 'how' y termina con exclamación.",
        "ejemplo_en": "How great is this!",
        "ejemplo_es": "¡Qué genial es esto!"
    }
]

def mostrar_tabla():
    """Muestra la tabla de oraciones formateada."""
    print("--------------------------------------------------------------------------------------------------")
    print(f"{'Tipo de oración':<20} | {'Regla de redacción':<50} | {'Ejemplo en inglés':<20} | {'Traducción al español'}")
    print("--------------------------------------------------------------------------------------------------")
    for oracion in TABLA_ORACIONES:
        tipo = oracion["tipo"]
        regla = oracion["regla"]
        ejemplo_en = oracion["ejemplo_en"]
        ejemplo_es = oracion["ejemplo_es"]
        print(f"{tipo:<20} | {regla:<50} | {ejemplo_en:<20} | {ejemplo_es}")
    print("--------------------------------------------------------------------------------------------------")

def practicar():
    """Inicia el modo de práctica interactiva."""
    print("\n--- ¡Modo de Práctica! ---")
    print("Escribe la traducción de la oración que aparece. Si quieres salir, escribe 'salir'.")
    puntos = 0
    intentos = 0
    
    while True:
        # Selecciona una oración aleatoria de la tabla
        oracion_elegida = random.choice(TABLA_ORACIONES)
        
        # Decide aleatoriamente si se pide la versión en inglés o en español
        pregunta_en_espanol = random.choice([True, False])
        
        if pregunta_en_espanol:
            pregunta = oracion_elegida["ejemplo_es"]
            respuesta_correcta = oracion_elegida["ejemplo_en"]
            idioma_pregunta = "español"
            idioma_respuesta = "inglés"
        else:
            pregunta = oracion_elegida["ejemplo_en"]
            respuesta_correcta = oracion_elegida["ejemplo_es"]
            idioma_pregunta = "inglés"
            idioma_respuesta = "español"
        
        print(f"\nTraduce esta oración del {idioma_pregunta} al {idioma_respuesta}:")
        print(f"--> {pregunta}")
        
        respuesta_usuario = input("Tu respuesta: ").strip()
        
        if respuesta_usuario.lower() == "salir":
            print("\n¡Gracias por practicar! Hasta la próxima.")
            break
        
        intentos += 1
        # Compara las respuestas sin importar mayúsculas o minúsculas
        if respuesta_usuario.lower().strip() == respuesta_correcta.lower().strip():
            print("¡Correcto! ")
            puntos += 1
        else:
            print("Incorrecto. ")
            print(f"La respuesta correcta es: {respuesta_correcta}")
        
        print(f"Puntuación actual: {puntos}/{intentos}")
        
    print(f"\nResumen final: Conseguiste {puntos} de {intentos} traducciones correctas.")

if __name__ == "__main__":
    mostrar_tabla()
    practicar()
