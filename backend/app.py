from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

from db_handlers import database_is_empty, table_exists

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:secret_password@localhost:3306/kst_db"
db = SQLAlchemy(app)
CORS(app)


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


# create model tables if not exist
with app.app_context():
    # check if db is empty
    if database_is_empty(db):
        # created all model tables defined in the app
        db.create_all()
    # check if 'event' model table has been created successfully
    table_exists('event', db)


@app.route('/')
def hello():
    return "Hello world!"


def format_event(event):
    return {
        "description": event.description,
        "id": event.id,
        "created_at": event.created_at
    }


# create an event
@app.route('/events', methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)


# get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {"events": event_list}


# get single event
@app.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {"event": formatted_event}


# delete event
@app.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id {id} deleted!'


# update event
@app.route('/events/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description, created_at=datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:secret_password@localhost:3306/kst_db"
#     db = SQLAlchemy(app)
#     CORS(app)
