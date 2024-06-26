import json

def validate_emotion_value(value):
    if not -1 <= value <= 1:
        raise ValueError("The emotion value must be within the range [-1, 1].")

def modify_emotions(positive_emotions, negative_emotions, to_modify, percentage, increase=True):
    for emotion in to_modify:
        if emotion in positive_emotions:
            if increase:
                positive_emotions[emotion] = min(round(positive_emotions[emotion] * (1 + percentage / 100), 2), 1)
            else:
                positive_emotions[emotion] = max(round(positive_emotions[emotion] * (1 - percentage / 100), 2), 0)
        elif emotion in negative_emotions:
            if increase:
                negative_emotions[emotion] = min(round(negative_emotions[emotion] * (1 + percentage / 100), 2), 0)
            else:
                negative_emotions[emotion] = max(round(negative_emotions[emotion] * (1 - percentage / 100), 2), -1)
        else:
            raise ValueError(f"The emotion '{emotion}' does not exist in the emotions dictionary.")

def find_extremes(positive_emotions, negative_emotions):
    results = {
        'modified_positive_emotions': positive_emotions,
        'modified_negative_emotions': negative_emotions
    }

    total_positive_emotions = sum(positive_emotions.values())
    total_negative_emotions = sum(negative_emotions.values())

    if total_positive_emotions >= total_negative_emotions:
        if total_positive_emotions == 0:
            results['predominant_emotion'] = {"message": "No predominant emotions."}
        else:
            predominant_emotion = max(positive_emotions, key=positive_emotions.get)
            percentage_predominant = (positive_emotions[predominant_emotion] / total_positive_emotions) * 100
            results['predominant_emotion'] = {
                'emotion': predominant_emotion,
                'value': positive_emotions[predominant_emotion],
                'percentage': round(percentage_predominant, 2)
            }
    else:
        predominant_emotion = min(negative_emotions, key=negative_emotions.get)
        percentage_predominant = (negative_emotions[predominant_emotion] / total_negative_emotions) * 100
        results['predominant_emotion'] = {
            'emotion': predominant_emotion,
            'value': negative_emotions[predominant_emotion],
            'percentage': round(percentage_predominant, 2)
        }

    all_emotions = {**positive_emotions, **negative_emotions}
    lowest_emotion = min(all_emotions, key=all_emotions.get)
    results['lowest_emotion'] = {
        'emotion': lowest_emotion,
        'value': all_emotions[lowest_emotion]
    }

    return results

def increase_emotion(positive_emotions, negative_emotions, to_modify, percentage):
    modify_emotions(positive_emotions, negative_emotions, to_modify, percentage, increase=True)
    results = find_extremes(positive_emotions, negative_emotions)
    return results

def decrease_emotion(positive_emotions, negative_emotions, to_modify, percentage):
    modify_emotions(positive_emotions, negative_emotions, to_modify, percentage, increase=False)
    return find_extremes(positive_emotions, negative_emotions)

def normalize_emotions(emotions, target_min, target_max):
    normalized_emotions = {}
    for emotion, value in emotions.items():
        validate_emotion_value(value)
        normalized_value = (value + 1) * (target_max - target_min) / 2 + target_min
        normalized_emotions[emotion] = round(normalized_value, 2)
    return normalized_emotions

def change_emotions(positive_emotions, negative_emotions, to_modify, percentage):
    try:
        if to_modify == "positive":
            modify_emotions(positive_emotions, negative_emotions, positive_emotions.keys(), percentage, increase=True)
            modify_emotions(positive_emotions, negative_emotions, negative_emotions.keys(), percentage, increase=False)
        elif to_modify == "negative":
            modify_emotions(positive_emotions, negative_emotions, positive_emotions.keys(), percentage, increase=False)
            modify_emotions(positive_emotions, negative_emotions, negative_emotions.keys(), percentage, increase=True)
        else:
            raise ValueError("Invalid to_modify value. Use 'positive' or 'negative'.")

        total_positive_emotions = sum(positive_emotions.values())
        total_negative_emotions = sum(negative_emotions.values())
        positive_percentage = (total_positive_emotions / len(positive_emotions)) * 100
        negative_percentage = (total_negative_emotions / len(negative_emotions)) * 100

        results = {
            "modified_positive_emotions": positive_emotions,
            "modified_negative_emotions": negative_emotions,
            "positive_percentage": round(positive_percentage, 2),
            "negative_percentage": round(negative_percentage, 2)
        }

        return results

    except Exception as e:
        raise e

def lambda_handler(event, context):
    try:
        function = event.get('function')
        if function == 'increase_emotion':
            results = increase_emotion(
                event['positive_emotions'], 
                event['negative_emotions'], 
                event['to_modify'], 
                event['percentage']
            )

        elif function == 'decrease_emotion':
            results = decrease_emotion(
                event['positive_emotions'], 
                event['negative_emotions'], 
                event['to_modify'], 
                event['percentage']
            )

        elif function == 'normalize_emotions':
            emotions = {
                **event['positive_emotions'],
                **event['negative_emotions']
            }
            target_min = event['target_min']
            target_max = event['target_max']
            results = normalize_emotions(emotions, target_min, target_max)

        elif function == 'change_emotions':
            results = change_emotions(
                event['positive_emotions'],
                event['negative_emotions'], 
                event['to_modify'], 
                event['percentage']
            )

        else:
            return {'statusCode': 400, 'body': 'Invalid function'}

        return {'statusCode': 200, 'body': json.dumps(results)}

    except Exception as e:
        error_message = f'Error: {str(e)}'
        print(error_message)
        return {'statusCode': 400, 'body': json.dumps({'error': error_message})}
