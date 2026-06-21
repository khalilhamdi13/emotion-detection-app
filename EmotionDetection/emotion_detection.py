import requests

def emotion_detector(text_to_analyze):

    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, 400

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            url,
            json=input_json,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        formatted_response = response.json()

        emotions = formatted_response['emotionPredictions'][0]['emotion']

        dominant = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant

        return emotions, 200

    except requests.exceptions.RequestException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }, 500