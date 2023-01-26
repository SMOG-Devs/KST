from typing import List
import numpy as np
from kst_app.data_storage.models import Measurement, WeatherMeasurement


def batch_sensor_data_day(measurment_list: List[Measurement]) -> np.array:
    assert len(measurment_list) >= 24 * 50, 'not enough data'  # The number of measurments in one day
    last_24 = measurment_list[:24 * 50]

    batched_sensors = np.zeros([1, 24, 150])
    counter_sensors = 0
    counter_hours = 0
    for measurment in last_24:
        batched_sensors[0, counter_hours, counter_sensors * 3:(counter_sensors + 1) * 3] = [measurment.pm1,
                                                                                            measurment.pm25,
                                                                                            measurment.pm10]
        counter_sensors += 1
        if counter_sensors == 50:
            counter_sensors = 0
            counter_hours += 1

    return batched_sensors

def batch_sensor_data_week(measurment_list: List[Measurement], idx:int = None):
    if idx is None:
        last_week = measurment_list[-24*50*7:]
    else:
        last_week = measurment_list[idx:idx+24*50*7]
    assert len(last_week) >= 24 * 50 * 7, 'not enough data'

    batched_sensors = np.zeros([1, 24 * 7, 150])
    counter_sensors = 0
    counter_hours = 0
    for measurment in last_week:
        batched_sensors[0, counter_hours, counter_sensors * 3:(counter_sensors + 1) * 3] = [measurment.pm1,
                                                                                            measurment.pm25,
                                                                                            measurment.pm10]
        counter_sensors += 1
        if counter_sensors == 50:
            counter_sensors = 0
            counter_hours += 1

    return batched_sensors




def batch_auxiliary_data_day(measurment_list: List[WeatherMeasurement]) -> np.array:
    assert len(measurment_list) >= 24, 'not enough weather data'
    last_24 = measurment_list[0:24]

    batched_weather = np.zeros((1, 24, 10))

    for i, measurment in enumerate(last_24):
        batched_weather[0, i] = [measurment.rainLevel,
                                 measurment.temperature,
                                 measurment.humidity,
                                 measurment.pressure,
                                 measurment.windDirection,
                                 measurment.windSpeed,
                                 measurment.date.hour,
                                 measurment.date.day,
                                 measurment.date.month,
                                 measurment.date.year]

    return batched_weather

def batch_auxiliary_data_week(measurment_list: List[WeatherMeasurement], idx:int = None) -> np.array:
    if idx is None:
        last_week = measurment_list[-24*7:]
    else:
        last_week = measurment_list[idx:idx+24*7]

    assert len(last_week) >= 24 * 7, 'not enough weather data'

    batched_weather = np.zeros((1, 24*7, 10))

    for i, measurment in enumerate(last_week):
        batched_weather[0, i] = [measurment.rainLevel,
                                 measurment.temperature,
                                 measurment.humidity,
                                 measurment.pressure,
                                 measurment.windDirection,
                                 measurment.windSpeed,
                                 measurment.date.hour,
                                 measurment.date.day,
                                 measurment.date.month,
                                 measurment.date.year]

    return batched_weather
