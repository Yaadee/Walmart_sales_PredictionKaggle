import pandas as pd

# Read the weather data CSV file
weather_data = pd.read_csv("data/processed_data/weather_data.csv")
import pandas as pd

import pandas as pd

# Assuming weather_data[key] is already preprocessed
for key in weather_data.keys():
    if isinstance(weather_data[key], pd.DataFrame):  # Check if it's a DataFrame
        if 'Month' in weather_data[key].columns:  # Check if 'Month' column exists
            weather_data[key]['Month'].replace({'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                                                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12},
                                               inplace=True)
            weather_data[key]['Year'] = key
            weather_data[key]['date'] = pd.to_datetime(weather_data[key][['Year', 'Month', 'Day']], format='%y%m%d')
            weather_data[key]['date'] = weather_data[key]['date'].dt.to_period('M')
            weather_data[key]['WeatherEvent'].replace(to_replace=r'^[A-Za-z]', value=1, regex=True, inplace=True)
            weather_data[key]['WeatherEvent'].fillna(0, inplace=True)
            weather_data[key]['WeatherEvent'] = weather_data[key]['WeatherEvent'].astype('int64')
            weather_data[key].fillna(0, inplace=True)
            weather_data[key] = weather_data[key][['date', 'Temp avg (°C)', 'Dew Point avg (°C)', 'Humidity (%) avg',
                                                   'Sea Level Press. (hPa) high', 'Visibility (km) high', 'WeatherEvent',
                                                   'Wind (km/h) avg']]
            weather_data[key]['Temp avg (°C)'] = weather_data[key]['Temp avg (°C)'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key]['Dew Point avg (°C)'] = weather_data[key]['Dew Point avg (°C)'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key]['Humidity (%) avg'] = weather_data[key]['Humidity (%) avg'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key]['Sea Level Press. (hPa) high'] = weather_data[key]['Sea Level Press. (hPa) high'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key]['Visibility (km) high'] = weather_data[key]['Visibility (km) high'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key]['Wind (km/h) avg'] = weather_data[key]['Wind (km/h) avg'].apply(
                lambda x: float(x) if x != '-' else 0)
            weather_data[key].set_index('date', inplace=True)
            weather_event = weather_data[key].groupby('date')['WeatherEvent'].sum()
            weather_data[key] = weather_data[key].drop(columns=['WeatherEvent']).groupby('date').median()
            weather_data[key]['WeatherEvent'] = weather_event

            # Example: Print data types after processing
            print(f"Data types for year {key}:")
            print(weather_data[key].dtypes)
            print("\n")
        else:
            print(f"Month column not found in data for year {key}. Skipping processing.")
    else:
        print(f"Skipping key {key} as it's not a DataFrame.")
