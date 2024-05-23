# Desarrollo de un Toolkit con Computación Emocional Utilizando el Modelo Emocional de PANAS para la Detección y Análisis de Emociones

Este proyecto es un toolkit desarrollado como trabajo de grado por Isabella Marín Gutierrez y Monica Alexandra Prado. Está diseñado en Python y desplegado en AWS Lambda, con el objetivo de proporcionar una herramienta para la detección y análisis de emociones utilizando el modelo emocional de PANAS (Positive and Negative Affect Schedule) de Watson y Tellegen (1985).

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Funciones](#funciones)
- [Pruebas](#pruebas)
- [Licencia](#licencia)

## Descripción

El modelo emocional de PANAS se utiliza para representar y analizar las emociones humanas en términos de afectos positivos y negativos. Este toolkit permite manipular y analizar estas dimensiones emocionales utilizando varias funciones diseñadas para modificar y evaluar las emociones.

## Características

- Validación de valores emocionales dentro de un rango específico.
- Modificación de emociones (aumento y disminución) según un porcentaje dado.
- Análisis de emociones para encontrar la emoción predominante y la más baja.
- Normalización de emociones a un rango específico.
- Implementación en AWS Lambda para escalabilidad y accesibilidad.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/MonicAP10/Toolkit.git
    cd Toolkit
    ```

2. Configura tu entorno de Python e instala las dependencias necesarias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Despliega en AWS Lambda siguiendo las instrucciones de la [documentación de AWS](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html).

## Uso

### Estructura del Proyecto

- `main.py`: Archivo principal con la lógica de las funciones.
- `tests/`: Directorio que contiene las pruebas unitarias.

### Llamadas a la Lambda Function

Ejemplo de un evento para aumentar emociones y encontrar extremos:

```json
{
    "function": "increase_emotion",
    "positive_emotions": {"Entusiasta": 0.5},
    "negative_emotions": {"Hostil": 0.3},
    "to_modify": ["Entusiasta"],
    "percentage": 10
}
```
```
Respuesta Esperada
{
    "statusCode": 200,
    "body": {
        "modified_positive_emotions": {"Atento": 0.55},
        "modified_negative_emotions": {"Hostil": 0.3},
        "predominant_emotion": {"emotion": "Atento", "value": 0.55, "percentage": 100.0},
        "lowest_emotion": {"emotion": "Hostil", "value": 0.3}
    }
}
```
## Funciones
- validate_emotion_value(value): Valida que el valor de la emoción esté dentro del rango [-1, 1].
- modify_emotions(positive_emotions, negative_emotions, to_modify, percentage, increase=True): Modifica los valores de las emociones según el porcentaje dado.
- find_extremes(positive_emotions, negative_emotions): Encuentra la emoción predominante y la más baja.
- increase_emotion(positive_emotions, negative_emotions, to_modify, percentage): Aumenta emociones y encuentra extremos.
- decrease_emotion(positive_emotions, negative_emotions, to_modify, percentage): Disminuye emociones y encuentra extremos.
- normalize_emotions(emotions, target_min, target_max): Normaliza los valores de las emociones al rango especificado.
change_emotions(positive_emotions, negative_emotions, to_modify, percentage): Cambia las emociones positivas o negativas según el porcentaje dado.

Estas funciones se encuentran de manera detallada en https://sites.google.com/correounivalle.edu.co/toolkit-modelo-emocional-panas/toolkit-documentation
## Pruebas
Las pruebas unitarias se encuentran en el directorio tests/. Utilizamos pytest para ejecutar las pruebas.

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
  pytest
```
Cobertura de Pruebas
- validate_emotion_value: Verifica que los valores emocionales estén dentro del rango permitido.
- increase_emotions: Aumenta las emociones y encuentra las emociones extremas.
- decrease_emotion: Disminuye las emociones y encuentra las emociones extremas.
- normalize_emotions: Normaliza los valores emocionales al rango objetivo.
- change_emotions: Cambia las emociones según el tipo y porcentaje especificado.
- lambda_handler: Verifica la lógica de la función Lambda para distintos casos de uso.

## Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT.
