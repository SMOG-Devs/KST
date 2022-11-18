from sqlalchemy import inspect


def database_is_empty(db):
    table_names = db.inspect(db.engine).get_table_names()
    is_empty = table_names == []
    print('Db is empty: {}'.format(is_empty))
    return is_empty


def table_exists(name, db):
    ret = inspect(db.engine).has_table(name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret
