import pandas as pd
import os

def convert_excel_to_csv(excel_path, csv_name, processed_data_dir="data/processed_data"):
    df = pd.read_excel(excel_path)
    csv_path = os.path.join(processed_data_dir, f"{csv_name}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Converted {excel_path} to {csv_path}")

if __name__ == "__main__":
    processed_data_dir = "data/processed_data"
    os.makedirs(processed_data_dir, exist_ok=True)

    files_to_convert = {
        "macro_economic": "data/raw_data/macro_economic.xlsx",
        "events_Holidays_data": "data/raw_data/Events_HolidaysData.xlsx",
        "weather_data": "data/raw_data/WeatherData.xlsx",
        "attributes_description": "data/raw_data/attributes_description.xlsx"
    }

    for csv_name, excel_path in files_to_convert.items():
        convert_excel_to_csv(excel_path, csv_name, processed_data_dir)

    # Copy train.csv and Kaggle_Submission_Format.csv directly as they are already in CSV format
    train_csv = "data/raw_data/train.csv"
    kaggle_submission_csv = "data/raw_data/Kaggle_Submission_Format.csv"
    submission_csv ="data/raw_data/submission.csv"
    
    train_df = pd.read_csv(train_csv)
    train_df.to_csv(os.path.join(processed_data_dir, "train.csv"), index=False)
    
    submission_format_df = pd.read_csv(kaggle_submission_csv)
    submission_format_df.to_csv(os.path.join(processed_data_dir, "Kaggle_Submission_Format.csv"), index=False)

    submission_df = pd.read_csv(submission_csv)
    submission_df.to_csv(os.path.join(processed_data_dir, "Submission.csv"), index=False)

    print(f"Copied {train_csv} to {os.path.join(processed_data_dir, 'train.csv')}")
    print(f"Copied {kaggle_submission_csv} to {os.path.join(processed_data_dir, 'Kaggle_Submission_Format.csv')}")
    print(f"Copied {submission_csv} to {os.path.join(processed_data_dir, 'Submission.csv')}")
