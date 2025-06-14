import csv
import os
import re
from utils.validacion_password import validar_password

def cargar_usuarios(ruta_archivo):
    """
    Carga los nombres de usuario desde el archivo CSV.

    Retorna:
    - Un conjunto con todos los nombres de usuario registrados.
    """
    usuarios = set()
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila:
                    usuarios.add(fila[0])  # Solo se guarda el nombre de usuario
    return usuarios

def guardar_usuario(ruta_archivo, nombre_usuario, password):
    """
    Agrega un nuevo usuario al archivo CSV.

    Parámetros:
    - nombre_usuario: string con el nombre de usuario
    - password: contraseña del usuario (en texto plano, por simplicidad en este ejercicio)
    """
    with open(ruta_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre_usuario, password])

def registrar_usuario(ruta_archivo):
    """
    Permite registrar un nuevo usuario.

    - Verifica que el nombre de usuario no exista previamente.
    - Solicita una contraseña y la valida utilizando una función externa.
    - Si la contraseña es válida, guarda el nuevo usuario y retorna su nombre.
    """
    print("=== REGISTRAR NUEVO USUARIO ===")
    usuarios_existentes = cargar_usuarios(ruta_archivo)

    # Solicita nombre de usuario no repetido
    while True:
        username = input("Elegí un nombre de usuario: ").strip()
        if username in usuarios_existentes:
            print("Ese nombre de usuario ya existe. Elegí otro.\n")
        else:
            break

    # Solicita y valida contraseña
    while True:
        password = input("Ingresá una contraseña: ").strip()
        valido, errores = validar_password(password)
        if valido:
            guardar_usuario(ruta_archivo, username, password)
            print("Usuario registrado exitosamente.\n")
            return username  # Realiza login automático tras el registro
        else:
            print("La contraseña no es segura. Motivos:")
            for error in errores:
                print(f"  - {error}")
            print("Recomendación: Usá al menos 8 caracteres, incluyendo una mayúscula y un número.\n")
