from salary import SalaryPredictor
from sentiment import SentimentPredictor

predictors = [SalaryPredictor(), SentimentPredictor()]

input_data = {
    "years": 3,
    "text": 'This is good'
}
for predictor in predictors:
    print(predictor.predict(input_data))