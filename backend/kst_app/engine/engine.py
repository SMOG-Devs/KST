from kst_app import app
from kst_app.data_storage.models import Measurement, add_measurements, Sensor, add_sensor


def add_measurement():
    # add measurements
    # list_of_measurements = []
    # measurement = Measurement(1, 2, 2.5, 0, 0, 0, '2020-01-01', 2)
    # list_of_measurements.append(measurement)
    #
    # sensor = Sensor(123.5, 121.2)
    with app.app_context():
        # add_measurements(list_of_measurements)
        add_sensor(123.5, 121.2)


if __name__ == '__main__':
    add_measurement()
