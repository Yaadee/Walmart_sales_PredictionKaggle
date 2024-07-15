# Sales Prediction Project
This project aims to predict sales for various clothing categories (Women, Men, and Other) using historical sales data and additional macroeconomic indicators. The analysis involves data preprocessing, feature engineering, model training, and evaluation. The final implementation is done in a Jupyter notebook (Sales_predictions.ipynb)


.
├── data
│   ├── processed_data
│   │   ├── attributes_description.csv
│   │   ├── events_Holidays_data.csv
│   │   ├── Kaggle_Submission_Format.csv
│   │   ├── macro_economic.csv
│   │   ├── Submission.csv
│   │   ├── train.csv
│   │   └── weather_data.csv
│   ├── processed_data.dvc
│   └── raw_data
│       ├── attributes_description.xlsx
│       ├── Events_HolidaysData.xlsx
│       ├── Kaggle_Submission_Format.csv
│       ├── macro_economic.xlsx
│       ├── submission.csv
│       ├── train.csv
│       └── WeatherData.xlsx
├── models
│   ├── evaluate_model.py
│   └── train_model.py
├── notebook
│   ├── Sales_predictions.ipynb
│   ├── submission.csv
│   └── submission.csv.dvc
├── predictions
├── README.md
├── requirements.txt
├── result_plots
├── Sales_prediction.ipynb
└── src
    ├── data_analysis.py
    ├── Feature_engineering.py
    └── preprocess.py
This is the project strucuture but for now it is implemented in Sales_predictions.ipynb



# Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.10.12 
Jupyter Notebook
DVC (Data Version Control)
Required Python packages listed in requirements.txt
Installation
Clone the repository:


git clone https://github.com/Yaadee/Walmart_sales_PredictionKaggle.git
cd Walmart_sales_PredictionKaggl

 # Install dependencies:


pip install -r requirements.txt
Set up DVC:

dvc pull

jupyter notebook notebook/Sales_predictions.ipynb


# Kaggle submitted link 

https://www.kaggle.com/yadasatarafa
