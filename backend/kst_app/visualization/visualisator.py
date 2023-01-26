import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap
from datetime import datetime, timedelta
from kst_app.data_storage.models import Measurement, Sensor
from kst_app import app


def create_heatmap(start_date: str = None, end_date: str = None):
    print(f'Start: {start_date}, end: {end_date}')

    with app.app_context():
        sensors = Sensor.query.all()
        # filter data from db
        if start_date is None or end_date is None or start_date == 'None' or end_date == 'None':
            measurements = Measurement.query.all()
        else:
            measurements = Measurement.query.filter(Measurement.date.between(start_date, end_date)).all()

    # create dataframe
    # print(measurements)
    for measurement in measurements:
        print('measurement: ', measurement.date, measurement.pm1, measurement.pm25, measurement.pm10)

    for sensor in sensors:
        print('sensor: ', sensor.id, sensor.latitude, sensor.longitude)

    df = pd.DataFrame([(measurement.date, measurement.pm1, measurement.pm25, measurement.pm10, sensor.latitude, sensor.longitude) for measurement in measurements for sensor in sensors if measurement.sensor_id == sensor.id], columns=['timestamp', 'PM1', 'PM25', 'PM10', 'latitude', 'longitude'])
    # df = pd.DataFrame([m.to_dict() for m in measurements])
    print(df)
    # create heatmap

    # sample data based on which the visualisations are created
    # day1 = pd.read_pickle(r'kst_app/visualization/notebooks/measurements/oneday.pickle')
    # day2 = pd.read_pickle(r'kst_app/visualization/notebooks/measurements/oneday2.pickle')

    # 1 hour, in each hour data from sensors
    # each tuple data: (pm1, pm10, pm25, longitude, latitude)
    # print(f"Count of sensors measuring air quality: {len(day1[0])}")

    air_df = df
    # time = datetime(2022, 12, 20)
    # air_df = pd.DataFrame(columns=['PM1', 'PM10', 'PM25', 'latitude', 'longitude'])
    #
    # for day in [day1, day2]:
    #     for hour_data in day:
    #         new_df = pd.DataFrame(hour_data, columns=['PM1', 'PM10', 'PM25', 'latitude', 'longitude'])
    #         new_df['timestamp'] = time
    #         time = time + timedelta(hours=1)
    #         air_df = pd.concat([air_df, new_df])

    pm1_data = []
    for time in air_df['timestamp'].unique():
        temp = []
        for index, record in air_df[air_df['timestamp'] == time].iterrows():
            temp.append([record['longitude'], record['latitude'], record['PM1']])
        pm1_data.append(temp)

    # create normal map
    krakow_coords = [50.0496863, 19.944544]
    map_krakow = folium.Map(krakow_coords, zoom_start=13)

    # create heatmap
    hm = plugins.HeatMapWithTime(
        pm1_data,
        display_index=True,
        index=air_df['timestamp'].apply(lambda timestamp: str(timestamp)).unique().tolist(),
        auto_play=True,
        radius=30,
        use_local_extrema=True,
    )
    # add heatmap on map
    hm.add_to(map_krakow)

    # map as html
    html_map = map_krakow.get_root().render()
    return html_map
