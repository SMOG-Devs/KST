from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def table_exists(name):
    ret = inspect(db.engine).has_table(name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret


def database_is_empty():
    table_names = db.inspect(db.engine).get_table_names()
    is_empty = table_names == []
    print('Db is empty: {}'.format(is_empty))
    return is_empty
