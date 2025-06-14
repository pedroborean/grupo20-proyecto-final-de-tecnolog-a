import csv
import os
from collections import Counter

def mostrar_estadisticas_globales(ruta_historial):
    """
    Calcula y muestra estadísticas globales a partir del archivo de historial climático.

    Incluye:
    - Total de consultas realizadas
    - Ciudad más consultada
    - Temperatura promedio registrada

    También indica que el archivo CSV puede utilizarse en herramientas externas para análisis adicional.
    """

    if not os.path.exists(ruta_historial):
        print("No se encontró el archivo de historial.")
        return

    # Listas para acumular datos relevantes
    ciudades = []
    temperaturas = []
    total_consultas = 0

    # Lectura del archivo CSV de historial
    with open(ruta_historial, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            total_consultas += 1
            ciudades.append(fila["Ciudad"].strip().lower())
            try:
                temperaturas.append(float(fila["Temperatura_C"]))
            except ValueError:
                # Captura errores de conversión si los datos de temperatura no son válidos
                print(f"Temperatura inválida en fila: {fila}")
    
    # Validación de que existan datos válidos
    if not ciudades or not temperaturas:
        print("No hay datos suficientes para calcular estadísticas.")
        return

    # Cálculo de estadísticas básicas
    ciudad_mas_consultada = Counter(ciudades).most_common(1)[0][0]
    temperatura_promedio = round(sum(temperaturas) / len(temperaturas), 2)

    # Presentación de resultados en consola
    print("\nEstadísticas Globales de Consultas:\n")
    print(f"- Número total de consultas: {total_consultas}")
    print(f"- Ciudad más consultada: {ciudad_mas_consultada.title()}")
    print(f"- Temperatura promedio registrada: {temperatura_promedio} °C\n")

    # Sugerencia de uso posterior del CSV para análisis fuera de la aplicación
    print("El archivo historial_global.csv puede usarse en Excel. Están actualizados y disponibles para ser analizados.")
