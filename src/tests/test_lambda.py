import pytest
from src.main import * 

# Pruebas para la función validate_emotion_value 
def test_validate_emotion_value_valid(): 
    assert validate_emotion_value(0) is None 

def test_validate_emotion_value_invalid(): 
    with pytest.raises(ValueError): 
        validate_emotion_value(1.5) 

#___________________________________________________________________________________ 

def test_increase_emotion_and_find_extremes():
    positive_emotions = {'Atento': 0.5}
    negative_emotions = {'Hostil': 0.3}
    to_modify = ['Atento']
    percentage = 10
    result = increase_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage)
    assert result['modified_positive_emotions']['Atento'] == 0.55
    assert result['modified_negative_emotions']['Hostil'] == 0.3

def test_decrease_emotion_and_find_extremes():
    positive_emotions = {'Atento': 0.5}
    negative_emotions = {'Hostil': 0.3}
    to_modify = ['Atento']
    percentage = 10
    result = decrease_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage)
    assert result['modified_positive_emotions']['Atento'] == 0.45
    assert result['modified_negative_emotions']['Hostil'] == 0.3

#___________________________________________________________________________________
# Prueba para verificar el cálculo de la emoción predominante
def test_calculate_predominant_emotion():
    # Define datos de prueba
    negative_emotions = {'Molesto': -0.7, 'Inquieto': -0.5, 'Irritable': -0.3}
    total_negative_emotions = sum(negative_emotions.values())

    # Ejecuta la función que no tiene cobertura
    predominant_emotion = min(negative_emotions, key=negative_emotions.get)
    percentage_predominant = round((negative_emotions[predominant_emotion] / total_negative_emotions) * 100, 2)


    # Comprueba el resultado
    expected_emotion = 'Molesto'
    expected_value = -0.7
    expected_percentage = round((-0.7 / (-0.7 - 0.5 - 0.3)) * 100, 2)

    assert predominant_emotion == expected_emotion
    assert percentage_predominant == expected_percentage


#________________________________________________________________________________________ 

def test_normalize_emotions(): 
    # Caso 1: Emociones válidas y normalización exitosa 
    emotions = {'Atento': 0.8, 'Hostil': -0.5, 'Entusiasta': 0.7} 
    target_min = 0 
    target_max = 100 
    result = normalize_emotions(emotions, target_min, target_max) 
    assert result == {'Atento': 90.0, 'Hostil': 25.0, 'Entusiasta': 85.0} 

    # Caso 2: Emociones con valores extremos 
    emotions = {'Atento': 1.0, 'Hostil': -1.0, 'Entusiasta': 0.0} 
    target_min = 0 
    target_max = 10 
    result = normalize_emotions(emotions, target_min, target_max) 
    assert result == {'Atento': 10.0, 'Hostil': 0.0, 'Entusiasta': 5.0} 

    # Caso 3: Emociones con valores negativos y rango objetivo negativo 
    emotions = {'Atento': 0.8, 'Hostil': -0.5, 'Entusiasta': 0.7} 
    target_min = -50 
    target_max = 50 
    result = normalize_emotions(emotions, target_min, target_max) 
    assert result == {'Atento': 40.0, 'Hostil': -25.0, 'Entusiasta': 35.0} 

    # Caso 4: Emociones vacías 
    emotions = {} 
    target_min = 0 
    target_max = 100 
    result = normalize_emotions(emotions, target_min, target_max) 
    assert result == {} 

    # Caso 5: Emociones con valores fuera del rango [-1, 1] 
    emotions = {'Atento': 1.5, 'Hostil': -1.5, 'Entusiasta': 0.5} 
    target_min = 0 
    target_max = 100 
    with pytest.raises(ValueError): 
        normalize_emotions(emotions, target_min, target_max) 

#________________________________________________________________________________________ 

# Prueba para verificar el cambio de emociones positivas 
def test_change_positive_emotions(): 
    positive_emotions = {'Atento': 0.5, 'Entusiasta': 0.3} 
    negative_emotions = {'Hostil': -0.7} 
    to_modify = "positive" 
    percentage = 20 
    result = change_emotions(positive_emotions, negative_emotions, to_modify, percentage) 
    assert result['modified_positive_emotions']['Atento'] == 0.6 

# Prueba para verificar el cambio de emociones negativas 
def test_change_negative_emotions(): 
    positive_emotions = {'Atento': 0.5, 'Entusiasta': 0.3} 
    negative_emotions = {'Hostil': -0.7} 
    to_modify = "negative" 
    percentage = 20 
    result = change_emotions(positive_emotions, negative_emotions, to_modify, percentage) 
    assert result['modified_negative_emotions']['Hostil'] == -0.84 

# Prueba para verificar el manejo de un tipo de modificación inválido 
def test_invalid_modify_type(): 
    positive_emotions = {'Atento': 0.5, 'Entusiasta': 0.3} 
    negative_emotions = {'Hostil': -0.7} 
    to_modify = "invalid" 
    percentage = 20 
    with pytest.raises(ValueError): 
        change_emotions(positive_emotions, negative_emotions, to_modify, percentage) 

# Prueba para verificar que los valores de emoción no superen los límites de 1 y -1 
def test_emotion_value_limits(): 
    positive_emotions = {'Atento': 1.0} 
    negative_emotions = {'Hostil': -1.0} 
    to_modify = "positive" 
    percentage = 20 
    result = change_emotions(positive_emotions, negative_emotions, to_modify, percentage) 
    assert result['modified_positive_emotions']['Atento'] == 1.0  # Emoción positiva no debe exceder 1 
    assert result['modified_negative_emotions']['Hostil'] == -0.8  # Emoción negativa no debe exceder -1 

# Prueba para verificar el cálculo correcto de los porcentajes de emociones 
def test_percentage_calculation(): 
    positive_emotions = {'Atento': 0.5, 'Entusiasta': 0.3} 
    negative_emotions = {'Hostil': -0.7} 
    to_modify = "positive" 
    percentage = 20 
    result = change_emotions(positive_emotions, negative_emotions, to_modify, percentage) 
    assert result['positive_percentage'] == 48.0 
    assert result['negative_percentage'] == -56.0  # Porcentaje negativo debido a que solo hay una emoción negativa


# Prueba funcion de lambda handler
@pytest.mark.parametrize("event, expected_status, expected_body", [
    (
        {
            'function': 'increase_emotion_and_find_extremes',
            'positive_emotions': {'Atento': 0.5},
            'negative_emotions': {'Hostil': 0.3},
            'to_modify': ['Atento'],
            'percentage': 10
        },
        200,
        {
            'modified_positive_emotions': {'Atento': 0.55},
            'modified_negative_emotions': {'Hostil': 0.3},
            'predominant_emotion': {'emotion': 'Atento', 'value': 0.55, 'percentage': 100.0},
            'lowest_emotion': {'emotion': 'Hostil', 'value': 0.3}
        }
    ),
    (
        {
            'function': 'normalize_emotions',
            'positive_emotions': {'Atento': 0.5},
            'negative_emotions': {'Hostil': 0.3},
            'target_min': 0,
            'target_max': 1
        },
        200,
        {
            'Atento': 0.75,
            'Hostil': 0.65
        }
    ),
    (
        {
            'function': 'change_emotions',
            'positive_emotions': {'Atento': 0.5},
            'negative_emotions': {'Hostil': 0.3},
            'to_modify': 'positive',
            'percentage': 10
        },
        200,
        {
            'modified_positive_emotions': {'Atento': 0.55},
            'modified_negative_emotions': {'Hostil': 0.27},
            'positive_percentage': 55.0,
            'negative_percentage': 27.0
        }
    ),

    (
        {
            'function': 'decrease_emotion_and_find_extremes',
            'positive_emotions': {'Atento': 0.5},
            'negative_emotions': {'Hostil': 0.3},
            'to_modify': ['Atento'],
            'percentage': 10
        },
        200,
        {
            'modified_positive_emotions': {'Atento': 0.45},
            'modified_negative_emotions': {'Hostil': 0.3},
            'predominant_emotion': {'emotion': 'Atento', 'value': 0.45, 'percentage': 100.0},
            'lowest_emotion': {'emotion': 'Hostil', 'value': 0.3}
        }
    ),
    (
        {
            'function': 'invalid_function'
        },
        400,
        'Invalid function'
    )
])

# Prueba unitarias de lambda_handler
#_________________________________________________________________________________________________________________
def test_lambda_handler(event, expected_status, expected_body):
    response = lambda_handler(event, None)
    assert response['statusCode'] == expected_status
    if isinstance(expected_body, dict):
        assert json.loads(response['body']) == expected_body
    else:
        assert response['body'] == expected_body

def test_lambda_handler_exception_handling():
    # Caso 1: Simular una excepción cualquiera
    event = {'function': 'some_function', 'positive_emotions': {}, 'negative_emotions': {}, 'to_modify': [], 'percentage': 0}
    expected_status = 400
    expected_error_message = "Error: Some error message"  # Puedes personalizar el mensaje de error esperado
    with pytest.raises(Exception) as e:
        response = lambda_handler(event, None)
        assert response['statusCode'] == expected_status
        assert expected_error_message in response['body']

