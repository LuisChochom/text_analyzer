# text_analyzer
Este programa implementa un Analizador de Texto en Python utilizando estructuras básicas del lenguaje como strings, dict, set, manejo de excepciones, funciones y Programación Orientada a Objetos (POO).

El sistema permite:
Ingresar texto manualmente desde consola.
Seleccionar un archivo .txt mediante una interfaz gráfica (Tkinter).
Analizar el texto ingresado.
Generar un reporte estadístico en consola.
Realizar consultas interactivas sobre palabras específicas.

¿Qué hace el programa?
Una vez recibido el texto, el programa:

Normaliza el texto
  Convierte todo a minúsculas.
  Elimina signos de puntuación.
  Conserva únicamente caracteres alfanuméricos y espacios.

Tokeniza
  Divide el texto en palabras (tokens).

Calcula estadísticas
  Total de palabras.
  Cantidad de palabras únicas.
  Longitud promedio.
  Palabras más largas y más cortas.
  Top 10 palabras más frecuentes.

Permite consultas interactivas
  El usuario puede ingresar una palabra.
  El sistema muestra:
    Frecuencia
    Porcentaje respecto al total
    Clasificación:
      rara (1 vez)
      moderada (2–4 veces)
      común (5 o más veces)


Instrucciones de Ejecución

Requisitos
  Python 3.10 o superior
  Tkinter (incluido normalmente en Python estándar)


Ejecutar el programa
Desde la carpeta del proyecto:

python main.py


Flujo de ejecución

1. Elegir opción:
  1 → Ingresar texto manualmente
  2 → Seleccionar archivo .txt (abre ventana gráfica)
2. Se muestra el reporte.
3. Se habilita modo consulta:
  Ingresar palabra
  Escribir exit para salir

Pruebas Mínimas
Caso 1 – Texto simple
Entrada:

Hola hola mundo mundo mundo

Salida esperada:
  Total tokens: 5
  Tokens únicos: 2
  hola → 2
  mundo → 3
  mundo clasificada como "moderada"

Caso 2 – Archivo vacío
Debe mostrar:
Error: El archivo está vacío.

Caso 3 – Consulta sin existencia
Si se consulta una palabra inexistente:
La palabra 'x' no aparece en el texto.





