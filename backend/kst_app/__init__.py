from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from backend.kst_app.data_storage.routes import data_storage

app.register_blueprint(data_storage)

with app.app_context():
    db.create_all()

