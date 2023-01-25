from datetime import datetime
from typing import List

from backend.kst_app import db

'''
Sensors measuring the air quality. The data of sensors' measurements is extracted
and stored in the database. Based on those measurements the future air quality
is predicted by the prediction engine (neural network).
'''


class Sensor(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float(precision=10))
    latitude = db.Column(db.Float(precision=10))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # access to the measurements of the sensor
    measurements = db.relationship('Measurement', backref='sensor', lazy=True)
    predicted_measurements = db.relationship('PredictedMeasurement', backref='sensor', lazy=True)
    weather_measurement = db.relationship('WeatherMeasurement', backref='sensor', lazy=True)

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "created_at": self.created_at,
        }


def add_sensor(longitude: float, latitude: float) -> Sensor:
    sensor = Sensor(longitude, latitude)
    db.session.add(sensor)
    db.session.commit()
    return sensor


def add_sensors(sensors: List[Sensor]) -> List[Sensor]:
    db.session.add_all(sensors)
    db.session.commit()
    return sensors


def get_sensor(sensor_id: int) -> Sensor:
    sensor = Sensor.query.filter_by(id=sensor_id).one()
    return sensor


def get_all_sensors() -> List[Sensor]:
    return Sensor.query.all()


def delete_sensor(sensor_id: int) -> Sensor:
    sensor = Sensor.query.filter_by(id=sensor_id).one()
    db.session.delete(sensor)
    db.session.commit()
    return sensor


def update_sensor(sensor_id: int, longitude: float, latitude: float):
    sensor = Sensor.query.filter_by(id=sensor_id).one()
    if longitude is not None and latitude is not None:
        sensor.longitude = longitude
        sensor.latitude = latitude
    elif longitude is not None:
        sensor.longitude = longitude
    elif latitude is not None:
        sensor.latitude = latitude
    db.session.commit()
    return sensor


'''
Measurements from the sensors placed all over the city.
'''


class Measurement(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    pm1 = db.Column(db.Float(precision=10))
    pm25 = db.Column(db.Float(precision=10))
    pm10 = db.Column(db.Float(precision=10))
    pressure = db.Column(db.Float(precision=10))
    humidity = db.Column(db.Float(precision=10))
    temperature = db.Column(db.Float(precision=10))
    date = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

    def __init__(self, pm1, pm25, pm10, pressure, humidity, temperature, date, sensor_id):
        self.pm1 = pm1
        self.pm25 = pm25
        self.pm10 = pm10
        self.pressure = pressure
        self.humidity = humidity
        self.temperature = temperature
        self.date = date
        self.sensor_id = sensor_id

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "pm1": self.pm1,
            "pm25": self.pm25,
            "pm10": self.pm10,
            "pressure": self.pressure,
            "humidity": self.humidity,
            "temperature": self.temperature,
            "date": self.date,
            "sensor_id": self.sensor_id,
        }


def add_measurement(pm1: float, pm25: float, pm10: float, pressure: float, humidity: float, temperature: float,
                    date: datetime, sensor_id: int) -> Measurement:
    measurement = Measurement(pm1, pm25, pm10, pressure, humidity, temperature, date, sensor_id)
    db.session.add(measurement)
    db.session.commit()
    return measurement


def add_measurements(measurements: List[Measurement]) -> List[Measurement]:
    db.session.add_all(measurements)
    db.session.commit()
    return measurements


def get_measurement(measurement_id: int) -> Measurement:
    measurement = Measurement.query.filter_by(id=measurement_id).one()
    return measurement


def get_all_measurements() -> List[Measurement]:
    return Measurement.query.all()


def delete_measurement(measurement_id: int) -> Measurement:
    measurement = Measurement.query.filter_by(id=measurement_id).one()
    db.session.delete(measurement)
    db.session.commit()
    return measurement


def update_measurement(measurement_id: int, pm1: float, pm25: float, pm10: float, pressure: float, humidity: float,
                       temperature: float,
                       date: datetime, sensor_id: int) -> Measurement:
    measurement = Measurement.query.filter_by(id=measurement_id).one()
    if pm1 is not None:
        measurement.pm1 = pm1
    if pm25 is not None:
        measurement.pm25 = pm25
    if pm10 is not None:
        measurement.pm10 = pm10
    if pressure is not None:
        measurement.pressure = pressure
    if humidity is not None:
        measurement.humidity = humidity
    if temperature is not None:
        measurement.temperature = temperature
    if date is not None:
        measurement.date = date
    if sensor_id is not None:
        measurement.sensor_id = sensor_id
    db.session.commit()
    return measurement


'''
Future measurements predicted by the prediction engine.
In our case, the prediction engine is a neural network.
'''


class PredictedMeasurement(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    pm1 = db.Column(db.Float(precision=10))
    pm25 = db.Column(db.Float(precision=10))
    pm10 = db.Column(db.Float(precision=10))
    date = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

    def __init__(self, pm1, pm25, pm10, date, sensor_id):
        self.pm1 = pm1
        self.pm25 = pm25
        self.pm10 = pm10
        self.date = date
        self.sensor_id = sensor_id

    def to_json(self):
        return {
            "id": self.id,
            "pm1": self.pm1,
            "pm25": self.pm25,
            "pm10": self.pm10,
            "date": self.date,
            "sensor_id": self.sensor_id,
        }


def add_predicted_measurement(pm1: float, pm25: float, pm10: float,
                              date: datetime, sensor_id: int) -> PredictedMeasurement:
    predicted_measurement = PredictedMeasurement(pm1, pm25, pm10, date, sensor_id)
    db.session.add(predicted_measurement)
    db.session.commit()
    return predicted_measurement


def add_predicted_measurements(predicted_measurements: List[PredictedMeasurement]) -> List[PredictedMeasurement]:
    db.session.add_all(predicted_measurements)
    db.session.commit()
    return predicted_measurements


def get_predicted_measurement(measurement_id: int) -> PredictedMeasurement:
    predicted_measurement = PredictedMeasurement.query.filter_by(id=measurement_id).one()
    return predicted_measurement


def get_all_predicted_measurements() -> List[PredictedMeasurement]:
    return PredictedMeasurement.query.all()


def delete_predicted_measurement(measurement_id: int) -> PredictedMeasurement:
    predicted_measurement = PredictedMeasurement.query.filter_by(id=measurement_id).one()
    db.session.delete(predicted_measurement)
    db.session.commit()
    return predicted_measurement


def update_predicted_measurement(measurement_id: int, pm1: float, pm25: float, pm10: float,
                                 date: datetime, sensor_id: int) -> PredictedMeasurement:
    measurement = PredictedMeasurement.query.filter_by(id=measurement_id).one()
    if pm1 is not None:
        measurement.pm1 = pm1
    if pm25 is not None:
        measurement.pm25 = pm25
    if pm10 is not None:
        measurement.pm10 = pm10
    if date is not None:
        measurement.date = date
    if sensor_id is not None:
        measurement.sensor_id = sensor_id
    db.session.commit()
    return measurement


'''
Weather measurements from external API.
'''


class WeatherMeasurement(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(precision=10))
    humidity = db.Column(db.Float(precision=10))
    pressure = db.Column(db.Float(precision=10))
    windSpeed = db.Column(db.Float(precision=10))
    windDirection = db.Column(db.Float(precision=10))
    rainLevel = db.Column(db.Float(precision=10))
    date = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)

    def __init__(self, temperature, humidity, pressure, windSpeed, windDirection, rainLevel, date, sensor_id):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.windSpeed = windSpeed
        self.windDirection = windDirection
        self.rainLevel = rainLevel
        self.date = date
        self.sensor_id = sensor_id

    def to_json(self):
        return {
            "id": self.id,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "windSpeed": self.windSpeed,
            "windDirection": self.windDirection,
            "rainLevel": self.rainLevel,
            "date": self.date,
            "sensor_id": self.sensor_id
        }


def add_weather_measurement(temperature: float, humidity: float, pressure: float, windSpeed: float,
                            windDirection: float,
                            rainLevel: float, date: datetime, sensor_id: int) -> WeatherMeasurement:
    weather_measurement = WeatherMeasurement(temperature, humidity, pressure, windSpeed, windDirection, rainLevel, date,
                                             sensor_id)
    db.session.add(weather_measurement)
    db.session.commit()
    return weather_measurement


def add_weather_measurements(weather_measurements: List[WeatherMeasurement]) -> List[WeatherMeasurement]:
    db.session.add_all(weather_measurements)
    db.session.commit()
    return weather_measurements


def get_weather_measurement(measurement_id: int) -> WeatherMeasurement:
    weather_measurement = WeatherMeasurement.query.filter_by(id=measurement_id).one()
    return weather_measurement


def get_all_weather_measurements() -> List[WeatherMeasurement]:
    return WeatherMeasurement.query.all()


def delete_weather_measurement(measurement_id: int) -> WeatherMeasurement:
    weather_measurement = WeatherMeasurement.query.filter_by(id=measurement_id).one()
    db.session.delete(weather_measurement)
    db.session.commit()
    return weather_measurement


def update_weather_measurement(measurement_id: int, temperature: float, humidity: float, pressure: float,
                               windSpeed: float, windDirection: float,
                               rainLevel: float, date: datetime, sensor_id: int) -> WeatherMeasurement:
    measurement = WeatherMeasurement.query.filter_by(id=measurement_id).one()
    if temperature is not None:
        measurement.temperature = temperature
    if humidity is not None:
        measurement.humidity = humidity
    if pressure is not None:
        measurement.pressure = pressure
    if windSpeed is not None:
        measurement.windSpeed = windSpeed
    if windDirection is not None:
        measurement.windDirection = windDirection
    if rainLevel is not None:
        measurement.rainLevel = rainLevel
    if date is not None:
        measurement.date = date
    if sensor_id is not None:
        measurement.sensor_id = sensor_id
    db.session.commit()
    return measurement
