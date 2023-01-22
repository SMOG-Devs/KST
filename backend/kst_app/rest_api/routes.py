from flask import request, Blueprint, jsonify, after_this_request
from kst_app.data_storage.models import *
from kst_app.visualization.visualisator import create_heatmap

rest = Blueprint('rest', __name__)


# visualisation heatmap
@rest.route('/heatmap', methods=['GET'])
def get_heatmap():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    html_heatmap = create_heatmap()
    return html_heatmap
