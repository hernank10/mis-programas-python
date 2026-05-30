import random

homophones = {
    "La Tierra gira alrededor del Sol. (Gira vs. Jira)": "gira",
    "El médico le indicó que ingiriera más frutas y verduras. (Ingerir vs. Injerir)": "ingiriera",
    "Mi abuelo es un poco vejete. (Vejete vs. Vegete)": "vejete",
    "Para la cena preparé un delicioso gigote. (Gigote vs. Jigote)": "gigote",
    "Voy a grabar un video musical. (Grabar vs. Jabrar)": "grabar"
}

for sentence, answer in random.sample(homophones.items(), k=len(homophones)):
  print(sentence)
