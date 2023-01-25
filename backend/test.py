from kst_app.data_storage.models import Sensor, add_sensors
from kst_app import app
import pickle

if __name__ == '__main__':
    with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\data.pkl', 'rb') as port:
        data = pickle.load(port)

    with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\weather.pkl', 'rb') as port:
        weather = pickle.load(port)

    with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\sensors.pkl','rb') as port:
        sensors = pickle.load(port)

    list_of_sensors = []
    for key, value in sensors.items():
        sensor = Sensor(value['x'], value['y'])
        sensor.id = key
        list_of_sensors.append(sensor)

    with app.app_context():
        add_sensors(sensors)


    # list_of_measurments = []
    # for key, value in data.items():
    #     for id, info in value.items():
    #         measurment = Measurement(info[0], info[1], info[2], 0, 0, 0, key, id)
    #         list_of_measurments.append(list_of_measurments)
    #
    # add_measurements(list_of_measurments)
