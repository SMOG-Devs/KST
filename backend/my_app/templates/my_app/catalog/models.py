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


class PredictedMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pm1 = db.Column(db.Float(precision=10))
    pm25 = db.Column(db.Float(precision=10))
    pm10 = db.Column(db.Float(precision=10))
    date = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)


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
