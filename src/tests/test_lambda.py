import pytest 

from src.main import * 

 

# Pruebas para la función validate_emotion_value 

def test_validate_emotion_value_valid(): 

    assert validate_emotion_value(0) is None 

 

def test_validate_emotion_value_invalid(): 

    with pytest.raises(ValueError): 

        validate_emotion_value(1.5) 

#___________________________________________________________________________________ 

# Pruebas para la función increase_emotion_and_find_extremes 

def test_increase_emotion_and_find_extremes_function(): 

    positive_emotions = {'Atento': 0.5, 'Activo': -0.3} 

    negative_emotions = {'Avergonzado': -0.7} 

    to_modify = ['Atento', 'Activo'] 

    percentage = 10 

    result = increase_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage) 

    assert result['modified_positive_emotions'] == {'Atento': 0.55, 'Activo': -0.33} 

    assert result['modified_negative_emotions'] == {'Avergonzado': -0.7} 

    assert result['predominant_emotion']['emotion'] == 'Atento' 

    assert result['lowest_emotion']['emotion'] == 'Avergonzado' 

 

 

#________________________________________________________________________________________ 

 

# Prueba para la función decrease_emotion_and_find_extremes 

def test_decrease_emotion_and_find_extremes(): 

    positive_emotions = {'Atento': 0.8, 'Activo': -0.5} 

    negative_emotions = {'Avergonzado': -0.6} 

    to_modify = ['Atento'] 

    percentage = 20 

    result = decrease_emotion_and_find_extremes(positive_emotions, negative_emotions, to_modify, percentage) 

 

    # Verificar que las emociones positivas se han modificado correctamente 

    assert result['modified_positive_emotions'] == {'Atento': 0.64, 'Activo': -0.5} 

 

    # Verificar que las emociones negativas no se han modificado 

    assert result['modified_negative_emotions'] == {'Avergonzado': -0.6} 

 

    # Verificar que la emoción predominante es la misma que antes de la modificación 

    assert result['predominant_emotion']['emotion'] == 'Atento' 

 

    # Verificar que la emoción más baja es la misma que antes de la modificación 

    assert result['lowest_emotion']['emotion'] == 'Avergonzado' 

 

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

    assert result['negative_percentage'] == -56.0  # No hay emociones negativas modificadas en este caso 