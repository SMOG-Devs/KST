from TFModel import model, load_model, save_model
import kst_app.data_processing as process
from kst_app.data_storage import models as m
from backend.kst_app import app
from typing import List, Tuple
import numpy as np
from datetime import datetime


def predict_hour():
    data, weather = fetch_data()
    batched_data, batched_weather = batch_data(data, weather)

    last_measurment_date = weather[0].date

    load_model()
    out = model.predict([batched_data, batched_weather])
    save_model()

    save_record(out,last_measurment_date)


def fetch_data() -> Tuple[List[m.Measurement], List[m.WeatherMeasurement]]:
    return m.get_all_measurements(), m.get_weather_measurement()


def batch_data(data: List[m.Measurement], weather: List[m.WeatherMeasurement]) -> Tuple[np.array, np.array]:
    return process.batch_sensor_data_day(data), process.batch_auxiliary_data_day(weather)

def save_record(record: List[float], date: datetime):
    predicted_date = date.hour + 1
    list_of_ids = process.data_miner.mine_ids_sorted()
    list_of_predictions = []
    for i in range(0,len(record), 3):
        prediction = m.PredictedMeasurement(record[i], record[i+1], record[i+2], predicted_date, list_of_ids[i//3])
        list_of_predictions.append(prediction)
    with app.app_context():
        m.add_predicted_measurements(list_of_predictions)

