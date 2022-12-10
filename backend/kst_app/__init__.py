from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from kst_app.catalog.views import catalog

app.register_blueprint(catalog)

with app.app_context():
    db.create_all()
