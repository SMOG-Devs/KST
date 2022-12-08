from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from db_handlers import database_is_empty, table_exists
# ----
from extensions import db
from models import Event, Measurement, WeatherMeasurement, PredictedMeasurement


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:secret_password@localhost:3306/kst_db"
# db = SQLAlchemy(app)
# CORS(app)

# TODO:
#  - routing move to the rest_api file instead of creating it in `create_app` method
#  - `create_tables` should create all not existing tables, after Measurement table deletion it doesnt create the table during the run
#  - models might not be seen by db that's why it's not created - investigate it

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:secret_password@localhost:3306/kst_db"

    # ------ rest API ------
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

    # ------ rest API ------
    register_extensions(app)
    CORS(app)
    return app


def register_extensions(app):
    db.init_app(app)


# def create_tables(app):
#     with app.app_context():
#         # check if db is empty
#         if database_is_empty(db):
#             # created all model tables defined in the app
#             db.create_all()
#         # check if 'event' model table has been created successfully
#         table_exists('event', db)

def create_tables(app):
    with app.app_context():
        # create model tables if not exist
        db.create_all()
        # # check if db is empty
        # if database_is_empty(db):
        #     # created all model tables defined in the app
        #     db.create_all()
        # # check if 'event' model table has been created successfully
        # table_exists('event', db)


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

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:secret_password@localhost:3306/kst_db"
#     db = SQLAlchemy(app)
#     CORS(app)
