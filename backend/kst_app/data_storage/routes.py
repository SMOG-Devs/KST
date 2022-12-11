from flask import request, Blueprint
from kst_app.data_storage.models import *

data_storage = Blueprint('data_storage', __name__)


@data_storage.route('/')
@data_storage.route('/home')
def hello():
    return "Hello world!"


#      Sensor

# add new sensor
@data_storage.route('/sensor', methods=['POST'])
def add_sensor_route():
    added_sensor = add_sensor(
        request.json.get('longitude'),
        request.json.get('latitude')
    )
    return {"added_sensor": added_sensor.to_json()}


# get all sensors
@data_storage.route('/sensors', methods=['GET'])
def get_all_sensors_route():
    sensors = get_all_sensors()
    return {"sensors": list(map(lambda sensor: sensor.to_json(), sensors))}


# get sensor by id
@data_storage.route('/sensor/<sensor_id>', methods=['GET'])
def get_sensor_route(sensor_id: int):
    sensor = get_sensor(sensor_id)
    return {"sensor": sensor.to_json()}


# delete sensor by id
@data_storage.route('/sensor/<sensor_id>', methods=['DELETE'])
def delete_sensor_route(sensor_id: int):
    sensor = delete_sensor(sensor_id)
    return {"deleted_sensor": sensor.to_json()}


# update sensor by id
@data_storage.route('/sensor/<sensor_id>', methods=['PUT'])
def update_sensor_route(sensor_id: int):
    updated_sensor = update_sensor(
        sensor_id,
        request.json.get('longitude'),
        request.json.get('latitude')
    )
    return {"updated_sensor": updated_sensor.to_json()}


# create a measurement
@data_storage.route('/measurement', methods=['POST'])
def add_measurement_route():
    measurement = add_measurement(
        request.json.get('pm1'),
        request.json.get('pm25'),
        request.json.get('pm10'),
        request.json.get('pressure'),
        request.json.get('humidity'),
        request.json.get('temperature'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"added_measurement": measurement.to_json()}


# get all measurements
@data_storage.route('/measurements', methods=['GET'])
def get_measurements_route():
    measurements = get_all_measurements()
    return {"measurements": list(map(lambda measurement: measurement.to_json(), measurements))}


# get measurement by id
@data_storage.route('/measurement/<measurement_id>', methods=['GET'])
def get_measurement_route(measurement_id: int):
    measurement = get_measurement(measurement_id)
    return {"measurement": measurement.to_json()}


# delete measurement by id
@data_storage.route('/measurement/<measurement_id>', methods=['DELETE'])
def delete_measurement_route(measurement_id: int):
    measurement = delete_measurement(measurement_id)
    return {"deleted_measurement": measurement.to_json()}


# update measurement by id
@data_storage.route('/measurement/<measurement_id>', methods=['PUT'])
def update_measurement_route(measurement_id: int):
    updated_measurement = update_measurement(
        measurement_id,
        request.json.get('pm1'),
        request.json.get('pm25'),
        request.json.get('pm10'),
        request.json.get('pressure'),
        request.json.get('humidity'),
        request.json.get('temperature'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"updated_measurement": updated_measurement.to_json()}


#       Predicted Measurement

# add a measurement
@data_storage.route('/predicted-measurement', methods=['POST'])
def add_predicted_measurement_route():
    predicted_measurement = add_predicted_measurement(
        request.json.get('pm1'),
        request.json.get('pm25'),
        request.json.get('pm10'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"added_predicted_measurement": predicted_measurement.to_json()}


# get all predicted measurements
@data_storage.route('/predicted-measurements', methods=['GET'])
def get_predicted_measurements_route():
    predicted_measurements = get_all_predicted_measurements()
    return {"predicted_measurements": list(map(
        lambda predicted_measurement: predicted_measurement.to_json(),
        predicted_measurements
    ))}


# get predicted measurement by id
@data_storage.route('/predicted-measurement/<measurement_id>', methods=['GET'])
def get_predicted_measurement_route(measurement_id: int):
    predicted_measurement = get_predicted_measurement(measurement_id)
    return {"predicted_measurement": predicted_measurement.to_json()}


# delete predicted measurement by id
@data_storage.route('/predicted-measurement/<measurement_id>', methods=['DELETE'])
def delete_predicted_measurement_route(measurement_id: int):
    predicted_measurement = delete_predicted_measurement(measurement_id)
    return {"deleted_predicted_measurement": predicted_measurement.to_json()}


# update predicted measurement by id
@data_storage.route('/predicted-measurement/<measurement_id>', methods=['PUT'])
def update_predicted_measurement_route(measurement_id):
    updated_predicted_measurement = update_predicted_measurement(
        measurement_id,
        request.json.get('pm1'),
        request.json.get('pm25'),
        request.json.get('pm10'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"updated_predicted_measurement": updated_predicted_measurement.to_json()}


#       Weather measurement

# create a weather measurement
@data_storage.route('/weather-measurement', methods=['POST'])
def add_weather_measurement_route():
    weather_measurement = add_weather_measurement(
        request.json.get('temperature'),
        request.json.get('humidity'),
        request.json.get('pressure'),
        request.json.get('windSpeed'),
        request.json.get('windDirection'),
        request.json.get('rainLevel'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"added_weather_measurement": weather_measurement.to_json()}


# get all weather measurements
@data_storage.route('/weather-measurements', methods=['GET'])
def get_weather_measurements_route():
    weather_measurements = get_all_weather_measurements()
    return {"weather_measurements": list(map(
        lambda predicted_measurement: predicted_measurement.to_json(),
        weather_measurements
    ))}


# get single weather measurement by id
@data_storage.route('/weather-measurement/<measurement_id>', methods=['GET'])
def get_weather_measurement_route(measurement_id: int):
    weather_measurement = get_weather_measurement(measurement_id)
    return {"weather_measurement": weather_measurement.to_json()}


# delete predicted measurement by id
@data_storage.route('/weather-measurement/<measurement_id>', methods=['DELETE'])
def delete_weather_measurement_route(measurement_id: int):
    weather_measurement = delete_weather_measurement(measurement_id)
    return {"deleted_weather_measurement": weather_measurement.to_json()}


# update predicted measurement by id
@data_storage.route('/weather-measurement/<measurement_id>', methods=['PUT'])
def update_weather_measurement_route(measurement_id: int):
    updated_weather_measurement = update_weather_measurement(
        measurement_id,
        request.json.get('temperature'),
        request.json.get('humidity'),
        request.json.get('pressure'),
        request.json.get('windSpeed'),
        request.json.get('windDirection'),
        request.json.get('rainLevel'),
        request.json.get('date'),
        request.json.get('sensor_id')
    )
    return {"updated_weather_measurement": updated_weather_measurement.to_json()}
