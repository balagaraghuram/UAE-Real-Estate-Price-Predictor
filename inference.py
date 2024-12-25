import pandas as pd
import joblib

def predict_prices(model_path, input_path, output_path):
    model = joblib.load(model_path)
    df = pd.read_csv(input_path)

    predictions = model.predict(df)
    df["predicted_price"] = predictions

    df.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")
