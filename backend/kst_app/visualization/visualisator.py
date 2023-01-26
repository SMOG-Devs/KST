import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap
from datetime import datetime, timedelta
from kst_app.data_storage.models import Measurement, Sensor
from kst_app import app

import numpy as np
from scipy.interpolate import Rbf, RBFInterpolator


#  ---- interpolation ----
def scipy_idw(x, y, z, xi, yi):
    c = np.concatenate((x[:, None], y[:, None]), axis=1)
    t = RBFInterpolator(c, z)
    rs = t(np.vstack((xi, yi)).T)

    interp = Rbf(x, y, z, function='linear')
    # return interp(xi, yi)
    return t(np.concatenate((xi[:, None], yi[:, None]), axis=1))


def interpolate_pm(pm_data):
    heatmap = []
    for i in range(len(pm_data)):
        print("STOP")
        print(pm_data[i])
        yn, xn, zn = zip(*pm_data[i])
        print(pm_data[i])
        xn = np.asarray(xn)
        yn = np.asarray(yn)
        zn = np.asarray(zn)
        nx, ny = len(xn), len(yn)
        xi = np.linspace(xn.min(), xn.max(), nx)
        yi = np.linspace(yn.min(), yn.max(), ny)
        xi, yi = np.meshgrid(xi, yi)
        xi, yi = xi.flatten(), yi.flatten()
        gridn = scipy_idw(xn, yn, zn, xi, yi)
        gridn = gridn.reshape((ny, nx))

        # convert into list of (x, y, z)
        data = []
        for i in range(nx):
            for j in range(ny):
                data.append([xi[i], yi[j], gridn[i][j]])
        heatmap.append(data)
    return heatmap


# ---- interpolation ----


def create_heatmap(start_date: str = None, end_date: str = None):
    with app.app_context():
        sensors = Sensor.query.all()
        # filter data from db
        if start_date is None or end_date is None or start_date == 'None' or end_date == 'None':
            measurements = Measurement.query.all()
        else:
            measurements = Measurement.query.filter(Measurement.date.between(start_date, end_date)).all()

    #  logging
    # for measurement in measurements:
    #     print('measurement: ', measurement.date, measurement.pm1, measurement.pm25, measurement.pm10)
    # for sensor in sensors:
    #     print('sensor: ', sensor.id, sensor.latitude, sensor.longitude)

    df = pd.DataFrame(
        [(measurement.date, measurement.pm1, measurement.pm25, measurement.pm10, sensor.latitude, sensor.longitude) for
         measurement in measurements for sensor in sensors if measurement.sensor_id == sensor.id],
        columns=['timestamp', 'PM1', 'PM25', 'PM10', 'latitude', 'longitude'])
    print(df)

    # create heatmap
    air_df = df

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
