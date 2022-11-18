from datetime import datetime
from my_app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__(self, description):
        self.description = description


class Sensor(db.Model):
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


class Measurement(db.Model):
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


class PredictedMeasurement(db.Model):
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


class WeatherMeasurement(db.Model):
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
