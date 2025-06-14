import csv
import os

# Encabezados del archivo CSV donde se guarda el historial
ENCABEZADOS = [
    "NombreUsuario", "Ciudad", "FechaHora",
    "Temperatura_C", "Condicion_Clima",
    "Humedad_Porcentaje", "Viento_kmh"
]

def guardar_en_historial(ruta_historial, nombre_usuario, datos_clima):
    """
    Guarda una nueva entrada de clima en el archivo de historial global.

    - Crea el archivo si no existe.
    - Agrega encabezado si está vacío.
    - Añade una nueva fila con los datos del usuario y del clima actual.
    """
    archivo_nuevo = not os.path.exists(ruta_historial)
    debe_agregar_encabezado = True

    # Si el archivo ya existe, revisamos si contiene encabezado
    if not archivo_nuevo:
        with open(ruta_historial, "r", encoding="utf-8") as archivo:
            primera_linea = archivo.readline()
            debe_agregar_encabezado = not primera_linea.startswith("NombreUsuario")

    # Abrimos el archivo en modo append para agregar la nueva entrada
    with open(ruta_historial, "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)

        # Agregamos encabezado si corresponde
        if archivo_nuevo or debe_agregar_encabezado:
            escritor.writeheader()

        # Creamos la fila con los datos del usuario y clima
        fila = {
            "NombreUsuario": nombre_usuario,
            "Ciudad": datos_clima["Ciudad"],
            "FechaHora": datos_clima["FechaHora"],
            "Temperatura_C": datos_clima["Temperatura_C"],
            "Condicion_Clima": datos_clima["Condicion_Clima"],
            "Humedad_Porcentaje": datos_clima["Humedad_Porcentaje"],
            "Viento_kmh": datos_clima["Viento_kmh"]
        }

        # Guardamos la fila en el archivo
        escritor.writerow(fila)

    print("Consulta guardada en historial.\n")


def mostrar_historial_personal(ruta_historial, nombre_usuario, ciudad):
    """
    Filtra y muestra el historial climático del usuario para una ciudad específica.
    """
    if not os.path.exists(ruta_historial):
        print("El historial aún no existe.")
        return

    encontrados = []

    # Leemos todas las filas del historial y filtramos por usuario y ciudad
    with open(ruta_historial, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["NombreUsuario"].strip().lower() == nombre_usuario.strip().lower() and \
               fila["Ciudad"].strip().lower() == ciudad.strip().lower():
                encontrados.append(fila)

    if not encontrados:
        print(f"No se encontraron consultas previas de {nombre_usuario} para la ciudad '{ciudad}'.")
        return

    # Mostramos todas las consultas encontradas
    print(f"\nHistorial de {nombre_usuario} para la ciudad '{ciudad}':\n")
    for i, fila in enumerate(encontrados, start=1):
        print(f"{i}-Fecha/Hora: {fila['FechaHora']}")
        print(f"  Temperatura: {fila['Temperatura_C']} °C")
        print(f"  Condición: {fila['Condicion_Clima']}")
        print(f"  Humedad: {fila['Humedad_Porcentaje']}%")
        print(f"  Viento: {fila['Viento_kmh']} km/h\n")

