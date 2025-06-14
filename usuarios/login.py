import csv
import os

def cargar_usuarios(ruta_archivo):
    """
    Carga los usuarios desde un archivo CSV.

    Retorna:
    - Un diccionario con pares usuario:contraseña.
    - Si el archivo no existe, retorna un diccionario vacío.
    """
    usuarios = {}
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    usuario, contrasena = fila
                    usuarios[usuario] = contrasena
    return usuarios

def login(ruta_archivo):
    """
    Gestiona el proceso de inicio de sesión.

    - Solicita nombre de usuario y contraseña.
    - Valida contra el archivo de usuarios cargado previamente.
    - Permite hasta 3 intentos de autenticación.

    Retorna:
    - El nombre de usuario si la autenticación es exitosa.
    - None si falla después de 3 intentos o si el usuario abandona.
    """
    usuarios = cargar_usuarios(ruta_archivo)

    print("=== INICIAR SESIÓN ===")
    intentos = 0
    while True:
        nombre = input("Nombre de usuario: ").strip()
        clave = input("Contraseña: ").strip()

        # Verifica si las credenciales coinciden
        if nombre in usuarios and usuarios[nombre] == clave:
            print(f"\n¡Bienvenido/a {nombre}!\n")
            return nombre
        else:
            intentos += 1
            print("Usuario o contraseña incorrectos.\n")
            if intentos >= 3:
                print("Has excedido los intentos permitidos.")
                break
            opcion = input("¿Querés intentar de nuevo? (s/n): ").lower()
            if opcion != 's':
                break

    return None

# Bloque de prueba para ejecución directa del archivo
if __name__ == "__main__":
    usuario_logueado = login("usuarios_simulados.csv")
    if usuario_logueado:
        print("Accedés al Menú Principal...")
    else:
        print("Volviendo al Menú de Acceso.")
