from flask import request, Blueprint
from kst_app import db, app
from kst_app.data_storage.models import Sensor, Measurement, PredictedMeasurement, WeatherMeasurement

data_storage = Blueprint('data_storage', __name__)


@data_storage.route('/')
@data_storage.route('/home')
def hello():
    return "Hello world!"


#       Sensors

def format_sensor(sensor):
    return {
        "id": sensor.id,
        "longitude": sensor.longitude,
        "latitude": sensor.latitude,
        "created_at": sensor.created_at,
    }


# create a sensor
@data_storage.route('/sensor', methods=['POST'])
def create_sensor():
    longitude = request.json['longitude']
    latitude = request.json['latitude']
    sensor = Sensor(longitude, latitude)
    db.session.add(sensor)
    db.session.commit()
    return format_sensor(sensor)


# get all sensors
@data_storage.route('/sensors', methods=['GET'])
def get_sensors():
    sensors = Sensor.query.order_by(Sensor.id.asc()).all()
    sensors_list = []
    for sensor in sensors:
        sensors_list.append(format_sensor(sensor))
    return {"sensors": sensors_list}


# get single sensor
@data_storage.route('/sensor/<id>', methods=['GET'])
def get_sensor(id):
    sensor = Sensor.query.filter_by(id=id).one()
    formatted_sensor = format_sensor(sensor)
    return {"sensor": formatted_sensor}


# delete sensor
@data_storage.route('/sensor/<id>', methods=['DELETE'])
def delete_sensor(id):
    sensor = Sensor.query.filter_by(id=id).one()
    db.session.delete(sensor)
    db.session.commit()
    return f'Sensor (id {id}) deleted!'


# update sensor
@data_storage.route('/sensor/<id>', methods=['PUT'])
def update_sensor(id):
    sensor = Sensor.query.filter_by(id=id)
    longitude = request.json['longitude']
    latitude = request.json['latitude']
    sensor.update(dict(longitude=longitude, latitude=latitude))
    db.session.commit()
    return {'sensor': format_sensor(sensor.one())}


#       Measurement
def format_measurement(measurement):
    return {
        "id": measurement.id,
        "pm1": measurement.pm1,
        "pm25": measurement.pm25,
        "pm10": measurement.pm10,
        "pressure": measurement.pressure,
        "humidity": measurement.humidity,
        "temperature": measurement.temperature,
        "date": measurement.date,
        "sensor_id": measurement.sensor_id,
    }


# create a measurement
@data_storage.route('/measurement', methods=['POST'])
def create_measurement():
    pm1 = request.json['pm1']
    pm25 = request.json['pm25']
    pm10 = request.json['pm10']
    pressure = request.json['pressure']
    humidity = request.json['humidity']
    temperature = request.json['temperature']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    measurement = Measurement(pm1, pm25, pm10, pressure, humidity, temperature, date, sensor_id)
    db.session.add(measurement)
    db.session.commit()
    return format_measurement(measurement)


# get all measurements
@data_storage.route('/measurements', methods=['GET'])
def get_measurements():
    measurements = Measurement.query.order_by(Measurement.id.asc()).all()
    measurements_list = []
    for measurement in measurements:
        measurements_list.append(format_measurement(measurement))
    return {"measurements": measurements_list}


# get single measurement
@data_storage.route('/measurement/<id>', methods=['GET'])
def get_measurement(id):
    measurement = Measurement.query.filter_by(id=id).one()
    formatted_measurement = format_measurement(measurement)
    return {"measurement": formatted_measurement}


# delete measurement
@data_storage.route('/measurement/<id>', methods=['DELETE'])
def delete_measurement(id):
    measurement = Measurement.query.filter_by(id=id).one()
    db.session.delete(measurement)
    db.session.commit()
    return f'Measurement (id {id}) deleted!'


# update measurement
@data_storage.route('/measurement/<id>', methods=['PUT'])
def update_measurement(id):
    measurement = Measurement.query.filter_by(id=id)
    pm1 = request.json['pm1']
    pm25 = request.json['pm25']
    pm10 = request.json['pm10']
    pressure = request.json['pressure']
    humidity = request.json['humidity']
    temperature = request.json['temperature']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    measurement.update(
        dict(pm1=pm1, pm25=pm25, pm10=pm10, pressure=pressure, humidity=humidity, temperature=temperature, date=date,
             sensor_id=sensor_id))
    db.session.commit()
    return {'measurement': format_measurement(measurement.one())}


#   Predicted measurement

def format_predicted_measurement(predicted_measurement):
    return {
        "id": predicted_measurement.id,
        "pm1": predicted_measurement.pm1,
        "pm25": predicted_measurement.pm25,
        "pm10": predicted_measurement.pm10,
        "date": predicted_measurement.date,
        "sensor_id": predicted_measurement.sensor_id,
    }


# create a measurement
@data_storage.route('/predicted-measurement', methods=['POST'])
def create_predicted_measurement():
    pm1 = request.json['pm1']
    pm25 = request.json['pm25']
    pm10 = request.json['pm10']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    predicted_measurement = PredictedMeasurement(pm1, pm25, pm10, date, sensor_id)
    db.session.add(predicted_measurement)
    db.session.commit()
    return format_predicted_measurement(predicted_measurement)


# get all predicted measurements
@data_storage.route('/predicted-measurements', methods=['GET'])
def get_predicted_measurements():
    predicted_measurements = PredictedMeasurement.query.order_by(PredictedMeasurement.id.asc()).all()
    predicted_measurements_list = []
    for predicted_measurement in predicted_measurements:
        predicted_measurements_list.append(format_predicted_measurement(predicted_measurement))
    return {"predicted_measurements": predicted_measurements_list}


# get single predicted measurement
@data_storage.route('/predicted-measurement/<id>', methods=['GET'])
def get_predicted_measurement(id):
    predicted_measurement = PredictedMeasurement.query.filter_by(id=id).one()
    formatted_measurement = format_predicted_measurement(predicted_measurement)
    return {"measurement": formatted_measurement}


# delete predicted measurement
@data_storage.route('/predicted-measurement/<id>', methods=['DELETE'])
def delete_predicted_measurement(id):
    predicted_measurement = PredictedMeasurement.query.filter_by(id=id).one()
    db.session.delete(predicted_measurement)
    db.session.commit()
    return f'Predicted measurement (id {id}) deleted!'


# update predicted measurement
@data_storage.route('/predicted-measurement/<id>', methods=['PUT'])
def update_predicted_measurement(id):
    predicted_measurement = PredictedMeasurement.query.filter_by(id=id)
    pm1 = request.json['pm1']
    pm25 = request.json['pm25']
    pm10 = request.json['pm10']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    predicted_measurement.update(dict(pm1=pm1, pm25=pm25, pm10=pm10, date=date, sensor_id=sensor_id))
    db.session.commit()
    return {'measurement': format_predicted_measurement(predicted_measurement.one())}


#   Weather measurement

def format_weather_measurement(weather_measurement):
    return {
        "id": weather_measurement.id,
        "temperature": weather_measurement.temperature,
        "humidity": weather_measurement.humidity,
        "pressure": weather_measurement.pressure,
        "windSpeed": weather_measurement.windSpeed,
        "windDirection": weather_measurement.windDirection,
        "rainLevel": weather_measurement.rainLevel,
        "date": weather_measurement.date,
        "sensor_id": weather_measurement.sensor_id,
    }


# create a weather measurement
@data_storage.route('/weather-measurement', methods=['POST'])
def create_weather_measurement():
    temperature = request.json['temperature']
    humidity = request.json['humidity']
    pressure = request.json['pressure']
    windSpeed = request.json['windSpeed']
    windDirection = request.json['windDirection']
    rainLevel = request.json['rainLevel']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    weather_measurement = WeatherMeasurement(temperature, humidity, pressure, windSpeed, windDirection, rainLevel, date,
                                             sensor_id)
    db.session.add(weather_measurement)
    db.session.commit()
    return format_weather_measurement(weather_measurement)


# get all weather measurements
@data_storage.route('/weather-measurements', methods=['GET'])
def get_weather_measurements():
    weather_measurements = WeatherMeasurement.query.order_by(WeatherMeasurement.id.asc()).all()
    weather_measurements_list = []
    for weather_measurement in weather_measurements:
        weather_measurements_list.append(format_weather_measurement(weather_measurement))
    return {"weather_measurements": weather_measurements_list}


# get single weather measurement
@data_storage.route('/weather-measurement/<id>', methods=['GET'])
def get_weather_measurement(id):
    weather_measurement = WeatherMeasurement.query.filter_by(id=id).one()
    formatted_measurement = format_weather_measurement(weather_measurement)
    return {"weather_measurement": formatted_measurement}


# delete predicted measurement
@data_storage.route('/weather-measurement/<id>', methods=['DELETE'])
def delete_weather_measurement(id):
    weather_measurement = WeatherMeasurement.query.filter_by(id=id).one()
    db.session.delete(weather_measurement)
    db.session.commit()
    return f'Weather measurement (id {id}) deleted!'


# update predicted measurement
@data_storage.route('/weather-measurement/<id>', methods=['PUT'])
def update_weather_measurement(id):
    weather_measurement = WeatherMeasurement.query.filter_by(id=id)
    temperature = request.json['temperature']
    humidity = request.json['humidity']
    pressure = request.json['pressure']
    windSpeed = request.json['windSpeed']
    windDirection = request.json['windDirection']
    rainLevel = request.json['rainLevel']
    date = request.json['date']
    sensor_id = request.json['sensor_id']
    weather_measurement.update(dict(
        temperature=temperature, humidity=humidity, pressure=pressure,
        windSpeed=windSpeed, windDirection=windDirection, rainLevel=rainLevel,
        date=date, sensor_id=sensor_id))
    db.session.commit()
    return {'weather_measurement': format_weather_measurement(weather_measurement.one())}
