from app import create_app, create_tables
from flask import request

app = create_app()
create_tables(app)


# import rest api routes
# import rest_api

if __name__ == '__main__':
    app.run(debug=True)


# TODO: restAPI to be imported from the file not pasted as it is right now (see `app.py`)
