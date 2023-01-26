import pandas as pd
from flask import request, Blueprint, jsonify, after_this_request
from kst_app.data_storage.models import *
from kst_app.visualization.visualisator import create_heatmap
from kst_app import app

rest = Blueprint('rest', __name__)


# visualisation heatmap
# @rest.route('/heatmap', methods=['GET'])
# def get_heatmap():
#     @after_this_request
#     def add_header(response):
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
# 
#     html_heatmap = create_heatmap()
#     return html_heatmap


# @rest.route('/db_fill', methods=['GET'])
# def fill_data():
#     @after_this_request
#     def add_header(response):
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#
#     df_sensors = pd.read_csv('tests/csv/sensors.csv')
#     for index, row in df_sensors.iterrows():
#         print('SENSOR', row['sensor_id'], row['x'], row['y'])
#         add_sensor(row['sensor_id'], row['x'], row['y'])
#
#     df = pd.read_csv('tests/csv/measurements_prepared.csv')
#     for index, row in df.iterrows():
#         print(row['date'], row['pm1'], row['pm25'], row['pm10'], row['sensor_id'])
#         add_measurement(row['pm1'], row['pm25'], row['pm10'], 0, 0, 0, row['date'], row['sensor_id'])
#         # measurement = Measurement(date=row['date'], pm1=row['pm1'], pm25=row['pm25'], pm10=row['pm10'],
#         #                           sensor_id=row['sensor_id'], pressure=None, temperature=None, humidity=None)
#         # db.session.add(measurement)
#     #
#     # with app.app_context():
#     #     sensors = Sensor.query.all()
#     #     measurements = Measurement.query.all()
#     #     print(measurements)
#
#     print('FILL THE DATA!')
#     return 'FILL THE DATA!'


@rest.route('/heatmap/<start_date>/<end_date>', methods=['GET'])
def get_heatmap(start_date, end_date):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    html_heatmap = create_heatmap(start_date, end_date)
    return html_heatmap
