import re

def validar_password(password):

    errores = []

    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    if not re.search(r"[A-Z]", password):
        errores.append("Debe contener al menos una letra mayúscula.")

    if not re.search(r"\d", password):
        errores.append("Debe contener al menos un número.")

    es_valida = len(errores) == 0
    return es_valida, errores

def sugerencias_mejora():
    
    return [
        "Usá al menos 8 caracteres.",
        "Incluí una letra mayúscula.",
        "Incluí al menos un número.",
        # "Agregá caracteres especiales (!, @, #, etc.) para mayor seguridad."
    ]
