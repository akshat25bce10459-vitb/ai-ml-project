import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    try:
        data = pd.read_csv("student_data.csv")
    except Exception as e:
        print("CSV Error:", e)
        return None

    X = data[['difficulty', 'days_left']]
    y = data['priority']

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict_priority(model, difficulty, days_left):
    if model is None:
        return 0
    return model.predict([[difficulty, days_left]])[0]