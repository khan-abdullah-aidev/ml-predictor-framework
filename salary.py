from base import BasePredictor
class SalaryPredictor(BasePredictor):
    def predict(self, data):
        years = data["years"]
        return years * 10000
