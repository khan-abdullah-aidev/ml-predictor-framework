from base import BasePredictor
class SentimentPredictor(BasePredictor):
    def predict(self, data):
        text = data["text"].lower()
        if "good" in text:
            return "Positive"
        return "Negative"

