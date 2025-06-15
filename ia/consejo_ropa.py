import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde un archivo .env 
load_dotenv()

# Carga robusta de variables de entorno usando ruta absoluta (multiplataforma)
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

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
    f"Eres un asistente virtual especializado en consejos útiles e informales sobre vestimenta diaria. "
    f"Tu tarea es dar una recomendación práctica y breve (máximo 3 líneas) para que una persona sepa cómo vestirse hoy, "
    f"teniendo en cuenta el clima local. El estilo del consejo debe ser amigable, directo y comprensible para cualquier público.\n\n"
    f"Contexto: La ciudad es {datos_clima['Ciudad']} y el clima actual se caracteriza por: "
    f"{datos_clima['Condicion_Clima']}, {datos_clima['Temperatura_C']}°C, "
    f"{datos_clima['Humedad_Porcentaje']}% de humedad, y viento de {datos_clima['Viento_kmh']} km/h.\n\n"
    f"Instrucciones: Redacta solo el consejo de vestimenta, en tono informal, sin usar emojis ni repetir los datos del clima literalmente. "
    f"No hagas introducciones ni despedidas. Concéntrate en lo más relevante según el estado del tiempo.\n\n"
    f"Consejo:")

    try:
        # Solicitud de generación de contenido al modelo configurado
        respuesta = model.generate_content(prompt)
        return respuesta.text.strip()  # Se retorna el texto limpio de la respuesta
    
    except Exception as e:
        # Manejo genérico de errores, se retorna como mensaje para el usuario
        return f"Error al generar consejo IA: {e}"
