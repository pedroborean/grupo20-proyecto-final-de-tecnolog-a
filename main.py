from usuarios.login import login
from usuarios.registro import registrar_usuario
from clima.consulta_clima import consultar_clima
from clima.historial import guardar_en_historial
from clima.historial import mostrar_historial_personal
from estadisticas.estadisticas import mostrar_estadisticas_globales
import google.generativeai as genai
from ia.consejo_ropa import obtener_consejo_ia

import os


# RUTA del archivo CSV de usuarios
RUTA_USUARIOS = "usuarios/usuarios_simulados.csv"
RUTA_HISTORIAL = "clima/historial_global.csv"

def mostrar_menu_acceso():
    print("\n --Bienvenido a GuardiánClima-- ")
    print("1. Iniciar Sesión")
    print("2. Registrar Nuevo Usuario")
    print("3. Salir")

def mostrar_menu_principal(usuario):
    print(f"\n Menú Principal - Usuario: {usuario}")
    print("1. Consultar Clima Actual y Guardar en Historial")
    print("2. Ver Mi Historial Personal de Consultas por Ciudad")
    print("3. Estadísticas Globales de Uso y Exportar Historial Completo")
    print("4. Consejo IA: ¿Cómo Me Visto Hoy?")
    print("5. Acerca De...")
    print("6. Cerrar Sesión")

def menu_principal(usuario):
    while True:
        mostrar_menu_principal(usuario)
        opcion = input("Elegí una opción: ")

        if opcion == '1':
            ciudad = input(" Ingresá el nombre de la ciudad: ")
            datos_clima = consultar_clima(ciudad)
            if datos_clima:
                guardar_en_historial(RUTA_HISTORIAL, usuario, datos_clima)      
        
        elif opcion == '2':
            ciudad = input(" Ingresá el nombre de la ciudad: ")
            mostrar_historial_personal(RUTA_HISTORIAL, usuario, ciudad)
        elif opcion == '3':
            mostrar_estadisticas_globales("clima/historial_global.csv")
        elif opcion == "4":
            ciudad = input(" Ingresá la ciudad para generar el consejo: ")
            datos_clima = consultar_clima(ciudad)

            if datos_clima:
                consejo = obtener_consejo_ia(datos_clima)
                print("\nConsejo de Vestimenta generado por IA:\n")
                print(consejo)
                guardar_en_historial(RUTA_HISTORIAL, usuario, datos_clima)

        elif opcion == '5':
            print("\n      --Acerca de GuardiánClima--\n")
            print("Descripción general:")
            print("GuardiánClima ITBA es una aplicación de consola desarrollada con el objetivo de proporcionar información climática actualizada, permitir el seguimiento del historial de consultas")
            print("por usuario, generar estadísticas globales y brindar consejos personalizados mediante el uso de")
            print("inteligencia artificial.")

            print("\nUso del menú principal:")
            print("1. Consultar Clima Actual y Guardar en Historial:")
            print("   Permite ingresar una ciudad y consultar el clima actual utilizando la API de OpenWeather.")
            print("   La consulta se guarda en un archivo CSV junto con el usuario y la ciudad.")
            print("2. Ver Mi Historial Personal de Consultas por Ciudad:")
            print("   Muestra todas las consultas anteriores realizadas por el usuario para una ciudad específica.")
            print("3. Estadísticas Globales de Uso y Exportar Historial Completo:")
            print("   Recorre el historial completo y muestra la ciudad más consultada, el número total de consultas")
            print("   y la temperatura promedio global.")
            print("4. Consejo IA: ¿Cómo Me Visto Hoy?:")
            print("   Utiliza la API de Google Gemini para generar un consejo de vestimenta a partir del clima actual.")
            print("5. Acerca De:")
            print("   Describe el funcionamiento general de la aplicación.")
            print("6. Cerrar Sesión:")
            print("   Finaliza la sesión del usuario y retorna al menú de acceso.\n")

            print("Funcionamiento interno:")
            print("- Registro e inicio de sesión de usuarios: se realiza mediante archivos CSV. Durante el proceso,")
            print("  se valida que las contraseñas cumplan ciertos requisitos mínimos, como longitud adecuada y")
            print("  combinación de caracteres. Esto se debe a que contraseñas débiles son fácilmente vulnerables a ataques,")
            print("  lo que puede comprometer la integridad de los datos y la privacidad del usuario, incluso en sistemas")
            print("  de prueba. Por eso, se promueve el uso de contraseñas seguras como una buena práctica desde el diseño.")
            print("- Seguridad: las credenciales no están encriptadas ni protegidas. Se trata de un sistema simulado.")
            print("  En un entorno real, se recomienda el uso de funciones de hashing como bcrypt o Argon2 para proteger")
            print("  las contraseñas y otros datos sensibles.")
            print("- Clima e historial: se consulta la API de OpenWeather y los resultados se almacenan en un historial")
            print("  global CSV. Cada entrada incluye usuario, ciudad, fecha y condiciones meteorológicas.")
            print("- Estadísticas globales: a partir del historial CSV se pueden calcular métricas y se exportar los datos")
            print("  para posibles representaciones gráficas.")
            print("- Consejo personalizado: se emplea un modelo de lenguaje de Google Gemini para generar")
            print("  sugerencias de vestimenta basadas en el clima actual a partir de una cuidad le sea ingresada.\n")

            print("Desarrolladores del proyecto:")
            print("- Pedro Borean")
            print("- Augusto José Scaminaci")
            print("- Luis Vito Creatore")
            print("- Pedro Giordanino Cernicchiaro")
            print("- Xul Cielo Mizza Krasnobroda")

            print("Nombre del equipo de trabajo: Los MaTech\n")

        elif opcion == '6':
            print("Cerrando sesión... Volviendo al Menú de Acceso.")
            break
        else:
            print("Opción inválida. Elegí una opción del 1 al 6.")
        

def main():
    while True:
        mostrar_menu_acceso()
        opcion = input("Elegí una opción: ")

        if opcion == '1':
            usuario_logueado = login(RUTA_USUARIOS)
            if usuario_logueado:
                print(f"Usuario '{usuario_logueado}' autenticado correctamente.")
                menu_principal(usuario_logueado)
        elif opcion == '2':
            registrar_usuario(RUTA_USUARIOS)
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Elegí 1, 2 o 3.")

if __name__ == "__main__":
    main()

