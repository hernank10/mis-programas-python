import hunspell

def verificar_ortografia(palabra):
    hobj = hunspell.HunSpell('/usr/share/hunspell/es_ES.dic', '/usr/share/hunspell/es_ES.aff')
    return hobj.spell(palabra)

palabra = "cnidario"
if verificar_ortografia(palabra):
    print(f"{palabra} está escrita correctamente.")
else:
    print(f"{palabra} tiene un error ortográfico.")
