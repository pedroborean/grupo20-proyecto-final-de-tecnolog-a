# GuardiánClima ITBA

Aplicación de consola en Python que permite consultar el clima en tiempo real, almacenar un historial de consultas por usuario, generar estadísticas globales y obtener consejos personalizados de vestimenta a través de una IA (Gemini).

## Autores

Pedro Borean, Augusto José Scaminaci, Luis Vito Creatore, Pedro Giordanino Cernicchiaro y Xul Cielo Mizza Krasnobroda.

Grupo 20 - MaTech - Proyecto Final de Tecnología - ITBA


## Requisitos del entorno

Asegurate de tener instalado Python 3.11 o superior y de estar en la ruta correspondiente. Luego, seguí estos pasos:

1. Crear entorno virtual
# disclaimer! las veces que probamos en windows con el entorno virtual no funcionó. Preferentemente usarlo local en esta plataforma.
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows

2. Instalar dependencias
Primero asegurate de tener pip instalado con.
pip --version

En caso de que no te funcione el comando pip, podes ejecutarlo con python con:
py -m pip install -r requirements.txt


Instalá las bibliotecas necesarias con:

pip install -r requirements.txt

El archivo requirements.txt incluye las librerias:
- requests
- google-generativeai
- python-dotenv

## Ejecución del programa
Desde la raíz del proyecto, ejecutá en tu terminal:
python main.py

## Flujo del Menú
Menú de Acceso
- Iniciar sesión con usuario registrado
- Registrar nuevo usuario
- Salir de la app

## Menú Principal
- Consultar clima actual y guardar en historial
- Ver historial personal filtrado por ciudad
- Ver estadísticas globales de uso y exportar archivo CSV
- Obtener consejo de vestimenta generado por IA
- Ver información de la aplicación
- Cerrar sesión

## Configuración de API Keys
El proyecto utiliza dos APIs externas:
- OpenWeatherMap API: para obtener información del clima.
- Gemini (Google Generative AI): para generar recomendaciones de vestimenta.

1. Crear archivo .env
Debés crear un archivo .env (no incluido en el repositorio) con el siguiente contenido:
WEATHER_API_KEY=tu_clave_de_openweather
GEMINI_API_KEY=tu_clave_de_gemini

2. Compartir .env.template
Incluimos en el repositorio un archivo llamado .env.template con este contenido de ejemplo. En este caso para facilitar la corrección dejamos nuestras propias APIKEYS. Bastaría con renombrar el archivo unicamente a .env.

## Estructura del repositorio:
tp-final-tecno-grupo20/
├── clima/
│   ├── consulta_clima.py
│   ├── historial.py
│   └── historial_global.csv
├── estadisticas/
│   └── estadisticas.py
├── ia/
│   └── consejo_ropa.py
├── usuarios/
│   ├── login.py
│   ├── registro.py
│   └── usuarios_simulados.csv
├── utils/
│   └── validacion_password.py
├── main.py
├── .env.template
├── requirements.txt
└── README.md

## Seguridad
- Las claves se cargan mediante variables de entorno utilizando python-dotenv.
- Las contraseñas se almacenan en texto plano solo con fines educativos. En un entorno real, deben almacenarse con técnicas como hashing (bcrypt, argon2, etc.).
