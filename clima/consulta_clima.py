import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

# Carga las variables de entorno definidas en un archivo .env (por ejemplo, la API Key)
load_dotenv()

# Ruta absoluta al archivo .env (usando os.path para compatibilidad multiplataforma)
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

# Definición de la URL base para consultar el clima
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# obtiene la API Key desde las variables de entorno para evitar hardcodearla
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def consultar_clima(ciudad):
    # Define los parámetros de la consulta HTTP a la API de OpenWeatherMap
    params = {
        "q": ciudad,
        "appid": WEATHER_API_KEY,
        "units": "metric",  # solicita temperatura en grados Celsius
        "lang": "es"        # especifica que la respuesta sea en español
    }

    try:
        # Realiza la petición HTTP con los parámetros especificados
        respuesta = requests.get(BASE_URL, params=params)
        respuesta.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        datos = respuesta.json()  # Decodifica el contenido JSON de la respuesta

        # Extrae los datos necesarios de la respuesta
        temperatura = datos["main"]["temp"]
        condicion = datos["weather"][0]["description"]
        humedad = datos["main"]["humidity"]
        viento = datos["wind"]["speed"] * 3.6  # Conversión de m/s a km/h
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Muestra la información del clima por consola
        print(f"\nClima en {ciudad} ({fecha_hora}):")
        print(f"Temperatura: {temperatura} °C")
        print(f"Condición: {condicion}")
        print(f"Humedad: {humedad} %")
        print(f"Viento: {viento:.2f} km/h\n")

        # Guardado de datos en diccionario para estructurarlos
        return {
            "Ciudad": ciudad,
            "FechaHora": fecha_hora,
            "Temperatura_C": temperatura,
            "Condicion_Clima": condicion,
            "Humedad_Porcentaje": humedad,
            "Viento_kmh": round(viento, 2)
        }

    except requests.exceptions.HTTPError as errh:
        if respuesta.status_code == 401:
            print(f"Error de autenticación OWM: API Key inválida.")
        elif respuesta.status_code == 404:
            print(f"Error OWM: Ciudad '{ciudad}' no encontrada.")
        else:
            print(f"Error HTTP OWM: {errh}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Error de conexión/petición OWM: {err}")
        return None

    except json.JSONDecodeError:
        print("Error OWM: La respuesta de la API no es JSON válido.")
        return None
