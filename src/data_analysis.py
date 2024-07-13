import pandas as pd
# Load datasets
macro_data = pd.read_csv("data/processed_data/macro_economic.csv")
events_Holidays_data = pd.read_csv("data/processed_data/events_Holidays_data.csv")
weather_data = pd.read_csv("data/processed_data/weather_data.csv")
train_data = pd.read_csv("data/processed_data/train.csv")
test_data = pd.read_csv("data/processed_data/Submission.csv")
kaggle_submission_form = pd.read_csv("data/processed_data/Kaggle_Submission_Format.csv")


print("macro data",macro_data.columns)
print("Events and Holidays data", events_Holidays_data.columns)
print("Train data " , train_data.columns)
print("test data " , test_data.columns)
print("Kaggle submission data", kaggle_submission_form)
