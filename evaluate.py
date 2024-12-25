from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import pandas as pd

def evaluate_model(model_path, metrics):
    model = joblib.load(model_path)
    df = pd.read_csv("data/processed/cleaned_data.csv")

    X = df.drop("price", axis=1)
    y = df["price"]
    y_pred = model.predict(X)

    if "rmse" in metrics:
        print(f"RMSE: {mean_squared_error(y, y_pred, squared=False)}")
    if "mae" in metrics:
        print(f"MAE: {mean_absolute_error(y, y_pred)}")
    if "r2" in metrics:
        print(f"R2: {r2_score(y, y_pred)}")
V
