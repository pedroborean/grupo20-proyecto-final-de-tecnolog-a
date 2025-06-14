import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde un archivo .env 
load_dotenv()

# Configura la clave de API para el uso del modelo de Gemini desde las variables de entorno
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

# Se selecciona el modelo de Gemini a utilizar. En este caso: versión liviana y rápida.
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def obtener_consejo_ia(datos_clima):
    """
    Genera un consejo informal de vestimenta utilizando IA, basado en las condiciones climáticas actuales.

    Parámetros:
    - datos_clima (dict): Contiene información meteorológica como ciudad, temperatura, humedad, etc.

    Retorna:
    - Un string con el consejo generado por IA o un mensaje de error si ocurre alguna excepción.
    """

    # Armado del prompt de entrada a la IA, incluyendo los datos meteorológicos en lenguaje natural
    prompt = (
        f"Hola IA. Dame un consejo de vestimenta en 3 líneas máximo, "
        f"teniendo en cuenta que en {datos_clima['Ciudad']} hay {datos_clima['Condicion_Clima']}, "
        f"{datos_clima['Temperatura_C']}°C, {datos_clima['Humedad_Porcentaje']}% de humedad "
        f"y viento de {datos_clima['Viento_kmh']} km/h. "
        f"El consejo debe ser informal, pero útil."
    )

    try:
        # Solicitud de generación de contenido al modelo configurado
        respuesta = model.generate_content(prompt)
        return respuesta.text.strip()  # Se retorna el texto limpio de la respuesta
    
    except Exception as e:
        # Manejo genérico de errores, se retorna como mensaje para el usuario
        return f"Error al generar consejo IA: {e}"
