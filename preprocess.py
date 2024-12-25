 import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Example preprocessing steps
    df.dropna(inplace=True)
    df["area"] = df["area"].str.replace("sqft", "").astype(float)
    df = pd.get_dummies(df, columns=["location"], drop_first=True)

    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
