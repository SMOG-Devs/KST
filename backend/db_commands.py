from app import db
from sqlalchemy import inspect
from app import app


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


def create_model_tables():
    # create model tables if not exist
    with app.app_context():
        # check if db is empty
        if database_is_empty():
            # created all model tables defined in the app
            db.create_all()
        # check if 'event' model table has been created successfully
        table_exists('event')

# def database_is_empty(db):
#     table_names = db.inspect(db.engine).get_table_names()
#     is_empty = table_names == []
#     print('Db is empty: {}'.format(is_empty))
#     return is_empty
#
#
# def table_exists(name, db):
#     ret = inspect(db.engine).has_table(name)
#     print('Table "{}" exists: {}'.format(name, ret))
#     return ret
