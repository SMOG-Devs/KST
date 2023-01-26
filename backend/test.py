from kst_app.data_storage.models import Sensor, add_sensors, Measurement, add_measurements, delete_all_measurements, delete_all_weather_measurement,WeatherMeasurement, add_weather_measurements, get_all_measurements, get_all_weather_measurements
from kst_app import app
import pickle
import pandas

if __name__ == '__main__':

    # with app.app_context():
    #     print(delete_all_measurements())

    # with app.app_context():
    #     print(delete_all_weather_measurement())

    with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\data_dict.pickle', 'rb') as port:
        data = pickle.load(port)

    with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\weather_DF.pickle', 'rb') as port:
        weather = pickle.load(port)

    # with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\sensors.pkl','rb') as port:
    #     sensors = pickle.load(port)

    # list_of_sensors = []
    # for key, value in sensors.items():
    #     sensor = Sensor(value['x'], value['y'])
    #     sensor.id = key
    #     list_of_sensors.append(sensor)
    # print('done')

    # with app.app_context():
    #     add_sensors(list_of_sensors)
    # print('done')


    # list_of_measurments = []
    # for key, value in data.items():
    #     for id, info in value.items():
    #         measurment = Measurement(info[0], info[1], info[2], 0, 0, 0, key, id)
    #         list_of_measurments.append(measurment)
    # print('done')
    #
    # with app.app_context():
    #     add_measurements(list_of_measurments)
    # print('done')

    # with app.app_context():
    #     sensor = Sensor(0,0)
    #     sensor.id = 1
    #     add_sensors([sensor])


    # list_of_weather = []
    # weather = weather.drop(['hour','day','month','year'], axis=1).to_numpy()
    # for w in weather:
    #     list_of_weather.append(WeatherMeasurement(temperature=w[1], humidity=w[2],pressure=w[3], windSpeed=[5], windDirection=w[4],rainLevel=w[6], date=w[0], sensor_id=1))
    #
    # with app.app_context():
    #     add_weather_measurements(list_of_weather)
    # print('done')


