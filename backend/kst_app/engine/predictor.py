from kst_app.engine.TFModel import model, load_model, save_model, load_gustaw, save_gustaw
import kst_app.data_processing as process
from kst_app.data_storage import models as m
from kst_app import app
from typing import List, Tuple
import numpy as np
from datetime import datetime, timedelta


def predict_hour():
    data, weather = fetch_data()
    batched_data, batched_weather = batch_data_day(data, weather)

    last_measurment_date = weather[0].date

    load_model()
    out = model.predict([batched_data, batched_weather])
    save_model()

    save_record(out, last_measurment_date)


def predict_12h():
    delete_previous_predictions()

    data, weather = fetch_data()
    batched_data, batched_weather = batch_data_week(data, weather)

    last_measurment_date = weather[-1].date

    model = load_gustaw()
    out = model.predict([batched_data, batched_weather])
    save_gustaw(model)

    save_record_week(out, last_measurment_date)


def fetch_data() -> Tuple[List[m.Measurement], List[m.WeatherMeasurement]]:
    return m.get_all_measurements(), m.get_all_weather_measurements()

def delete_previous_predictions():
    m.delete_all_predicted_measurements()


def batch_data_day(data: List[m.Measurement], weather: List[m.WeatherMeasurement]) -> Tuple[np.array, np.array]:
    return process.batch_sensor_data_day(data), process.batch_auxiliary_data_day(weather)


def batch_data_week(data: List[m.Measurement], weather: List[m.WeatherMeasurement],idx:int = None) -> Tuple[np.array, np.array]:
    return process.batch_sensor_data_week(data,idx), process.batch_auxiliary_data_week(weather,idx)


def save_record(record: List[float], date: datetime):
    predicted_date = date.hour + 1
    list_of_ids = process.data_miner.mine_ids_sorted()
    list_of_predictions = []
    for i in range(0, len(record), 3):
        prediction = m.PredictedMeasurement(record[i], record[i + 1], record[i + 2], predicted_date,
                                            list_of_ids[i // 3])
        list_of_predictions.append(prediction)
    with app.app_context():
        m.add_predicted_measurements(list_of_predictions)


def save_record_week(record: np.array, date: datetime):
    print(record.shape)
    list_of_ids = process.data_miner.mine_ids_sorted()
    print(list_of_ids)
    list_of_predictions = []
    for i in range(12):
        predicted_date = date + timedelta(hours=i)
        for j in range(i*150,(i+1)*150 , 3):
            prediction = m.PredictedMeasurement(record[0,146+i,j], record[0,146+i,j + 1], record[0,146+i,j + 2], predicted_date,
                                                list_of_ids[(j - i * 150) // 3])
            list_of_predictions.append(prediction)
    print(len(list_of_predictions))
    with app.app_context():
        m.add_predicted_measurements(list_of_predictions)

def _predict_for_test(idx:int = None):
    data, weather = fetch_data()
    batched_data, batched_weather = batch_data_week(data, weather, idx)

    model = load_gustaw()
    out = model.predict([batched_data, batched_weather])
    save_gustaw(model)

    return out
