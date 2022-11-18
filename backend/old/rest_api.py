from datetime import datetime
from run import app
from flask import request
from extensions import db
from models import Event, Measurement, PredictedMeasurement, WeatherMeasurement


# @app.route('/')
# def hello():
#     return "Hello world!"
#
#
# def format_event(event):
#     return {
#         "description": event.description,
#         "id": event.id,
#         "created_at": event.created_at
#     }
#
#
# # create an event
# @app.route('/events', methods=['POST'])
# def create_event():
#     description = request.json['description']
#     event = Event(description)
#     db.session.add(event)
#     db.session.commit()
#     return format_event(event)
#
#
# # get all events
# @app.route('/events', methods=['GET'])
# def get_events():
#     events = Event.query.order_by(Event.id.asc()).all()
#     event_list = []
#     for event in events:
#         event_list.append(format_event(event))
#     return {"events": event_list}
#
#
# # get single event
# @app.route('/events/<id>', methods=['GET'])
# def get_event(id):
#     event = Event.query.filter_by(id=id).one()
#     formatted_event = format_event(event)
#     return {"event": formatted_event}
#
#
# # delete event
# @app.route('/events/<id>', methods=['DELETE'])
# def delete_event(id):
#     event = Event.query.filter_by(id=id).one()
#     db.session.delete(event)
#     db.session.commit()
#     return f'Event (id {id} deleted!'
#
#
# # update event
# @app.route('/events/<id>', methods=['PUT'])
# def update_event(id):
#     event = Event.query.filter_by(id=id)
#     description = request.json['description']
#     event.update(dict(description=description, created_at=datetime.utcnow()))
#     db.session.commit()
#     return {'event': format_event(event.one())}
