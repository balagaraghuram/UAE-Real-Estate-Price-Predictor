import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def train_model(model_name):
    df = pd.read_csv("data/processed/cleaned_data.csv")
    X = df.drop("price", axis=1)
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if model_name == "random_forest":
        model = RandomForestRegressor()
    else:
        raise ValueError(f"Model {model_name} not supported")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Model RMSE: {mean_squared_error(y_test, y_pred, squared=False)}")

    joblib.dump(model, "models/price_prediction_model.pkl")
    print("Model saved to models/price_prediction_model.pkl")
