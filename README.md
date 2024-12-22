# UAE-Real-Estate-Price-Predictor

# UAE Real Estate Price Predictor

This repository demonstrates how to **predict residential property prices** in various Emirates of the United Arab Emirates (e.g., Dubai, Abu Dhabi, Sharjah) using **machine learning models**. It utilizes historical data and features like location (city), property size (sqft), number of bedrooms/bathrooms, and amenities scores to estimate housing prices in AED (United Arab Emirates Dirhams).

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Data](#data)
- [Usage](#usage)
- [Model Training](#model-training)
- [Prediction](#prediction)
- [Example Commands](#example-commands)
- [Potential Improvements](#potential-improvements)
- [License](#license)

## Overview
Real estate in the UAE is a dynamic market, influenced by a variety of factors. This project aims to provide an **end-to-end workflow**:
1. **Data Preprocessing**  
2. **Model Training** (Linear Regression and Random Forest)  
3. **Price Prediction** (command-line interface or scripts)  
4. **Demonstration** using a brief animation (GIF) to illustrate model usage.

## Features
- **Data Preprocessing**: Clean and transform raw CSV data into a more usable format.
- **Multiple ML Models**: Compare performance between a baseline Linear Regression and a Random Forest Regressor.
- **Modular Code**: Separate scripts for data cleaning (`data_preprocessing.py`), model training (`train_model.py`), and inference (`predict.py`).
- **Animation**: A `.gif` (e.g., `price_prediction_demo.gif`) demonstrating how the project runs or how predictions are made.

## Project Structure

```bash
uae-real-estate-price-predictor/
├── data/
│   ├── raw_data.csv           # Original dataset with city, bedrooms, bathrooms, sqft, etc.
│   └── cleaned_data.csv       # Data after preprocessing
├── models/
│   ├── linear_regression.pkl
│   └── random_forest.pkl
├── src/
│   ├── data_preprocessing.py  # Script for cleaning/feature engineering
│   ├── train_model.py         # Script for training models
│   └── predict.py             # Script for making predictions
├── animations/
│   └── price_prediction_demo.gif  # Brief animation/GIF showing model usage
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
