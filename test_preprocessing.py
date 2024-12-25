import pandas as pd
from src.preprocess import preprocess_data

def test_preprocess_data():
    preprocess_data("data/raw/sample.csv", "data/processed/test_output.csv")
    df = pd.read_csv("data/processed/test_output.csv")
    assert "price" in df.columns
