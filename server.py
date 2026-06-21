from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect():

    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return "Invalid input! Please try again.", 400

    result, status = emotion_detector(text)

    if status != 200:
        return "Error processing request.", status

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response, 200


if __name__ == "__main__":
    app.run(debug=True)