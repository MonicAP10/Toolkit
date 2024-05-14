Toolkit es una biblioteca de Python diseñada para el procesamiento y modificación de datos emocionales. Proporciona diversas funciones para manipular y analizar emociones representadas como diccionarios de Python.

Estructura de Carpetas
src: Contiene el código fuente de la biblioteca.
main.py: Archivo principal que contiene las funciones principales para manipular emociones.
tests: Contiene los archivos de prueba para validar el funcionamiento de las funciones en main.py.
tests_lambda.py: Archivo que contiene las pruebas unitarias para las funciones de main.py.
__init__.py: Archivo que indica que tests es un paquete de Python.
venv: Carpeta virtual de entorno Python donde se instalan los paquetes y dependencias.
Descripción de Archivos
main.py: Contiene las funciones principales de Toolkit para modificar y analizar emociones. Cada función tiene una descripción de su entrada y salida en el código fuente.
tests_lambda.py: Archivo que incluye pruebas unitarias para las funciones en main.py, asegurando su correcto funcionamiento en diferentes escenarios.
__init__.py: Archivo que señala que tests es un paquete de Python, permitiendo la importación de sus funciones en otros archivos.
Funciones Principales
A continuación se describen las funciones principales de Toolkit junto con sus entradas y salidas:

validate_emotion_value(value)
Entrada: value (float) - El valor de la emoción a validar.
Salida: Ninguna.
Descripción: Valida que el valor de la emoción esté dentro del rango permitido [-1, 1].
modify_emotions(positive_emotions, negative_emotions, to_modify, percentage, increase=True)
Entrada:
positive_emotions (dict): Diccionario de emociones positivas.
negative_emotions (dict): Diccionario de emociones negativas.
to_modify (list): Lista de emociones a modificar.
percentage (float): Porcentaje de cambio a aplicar.
increase (bool, opcional): Indica si se aumentan o disminuyen las emociones (predeterminado: True).
Salida: Ninguna.
Descripción: Modifica las emociones positivas y negativas según el porcentaje especificado.
find_extremes(positive_emotions, negative_emotions)
Entrada:
positive_emotions (dict): Diccionario de emociones positivas.
negative_emotions (dict): Diccionario de emociones negativas.
Salida: Diccionario con las emociones modificadas y la emoción predominante.
Descripción: Encuentra la emoción predominante y la emoción más baja en los diccionarios de emociones.
increase_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage)
Entrada:
positive_emotions (dict): Diccionario de emociones positivas.
negative_emotions (dict): Diccionario de emociones negativas.
to_modify (list): Lista de emociones a modificar.
percentage (float): Porcentaje de aumento.
Salida: Resultados de find_extremes.
Descripción: Aumenta las emociones especificadas y encuentra las emociones extremas.
decrease_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage)
Entrada:
positive_emotions (dict): Diccionario de emociones positivas.
negative_emotions (dict): Diccionario de emociones negativas.
to_modify (list): Lista de emociones a modificar.
percentage (float): Porcentaje de disminución.
Salida: Resultados de find_extremes.
Descripción: Disminuye las emociones especificadas y encuentra las emociones extremas.
normalize_emotions(emotions, target_min, target_max)
Entrada:
emotions (dict): Diccionario de emociones a normalizar.
target_min (float): Valor mínimo deseado después de la normalización.
target_max (float): Valor máximo deseado después de la normalización.
Salida: Diccionario con las emociones normalizadas.
Descripción: Normaliza los valores de las emociones al rango especificado.
change_emotions(positive_emotions, negative_emotions, to_modify, percentage)
Entrada:
positive_emotions (dict): Diccionario de emociones positivas.
negative_emotions (dict): Diccionario de emociones negativas.
to_modify (str): Tipo de emociones a modificar ("positive" o "negative").
percentage (float): Porcentaje de cambio.
Salida: Diccionario con las emociones modificadas y porcentajes de emociones positivas y negativas.
Descripción: Cambia las emociones positivas o negativas según lo especificado y calcula los porcentajes correspondientes.
