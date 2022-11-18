import json
from datetime import datetime
from functools import wraps
from flask import request, Blueprint, render_template, jsonify
from my_app import db, app
from my_app.catalog.models import Event

catalog = Blueprint('catalog', __name__)



import json
from functools import wraps
from flask import request, Blueprint, render_template, jsonify, flash, \
    redirect, url_for, abort
from flask_restful import Resource, reqparse
from sqlalchemy.orm.util import join

from my_app import db, app, api

def template_or_json(template=None):
    """"Return a dict from your view and this will either
    pass it to a template or render json. Use like:
    @template_or_json('template.html')
    """

    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.is_xhr or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)

        return decorated_fn

    return decorated


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('price', type=float)
parser.add_argument('category', type=dict)


def template_or_json(template=None):
    """"Return a dict from your view and this will either
    pass it to a template or render json. Use like:
    @template_or_json('template.html')
    """
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)
        return decorated_fn
    return decorated


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@catalog.route('/')
@catalog.route('/home')
@template_or_json('home.html')
def home():
    return {'count': len('asd')}


@catalog.route('/product/<id>')
def product(id):
    return render_template('product.html', product=None)


@catalog.route('/products')
@catalog.route('/products/<int:page>')
def products(page=1):
    return render_template('products.html', products=None)


@catalog.route('/product-create', methods=['GET', 'POST'])
def create_product():
    return render_template('product-create.html')


@catalog.route('/product-search')
@catalog.route('/product-search/<int:page>')
def product_search(page=1):
    return render_template(
        'products.html', products=products.paginate(page, 10)
    )


@catalog.route('/category-create', methods=['POST',])
def create_category():
    return render_template('category.html', category=category)


@catalog.route('/category/<id>')
def category(id):
    return render_template('category.html', category=category)


@catalog.route('/categories')
def categories():
    return render_template('categories.html', categories=categories)


class ProductApi(Resource):

    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page, 10).items
        else:
            products = [Product.query.get(id)]
        if not products:
            abort(404)
        res = {}
        for product in products:
            res[product.id] = {
                'name': product.name,
                'price': product.price,
                'category': product.category.name
            }
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        categ_name = args['category']['name']
        category = Category.query.filter_by(name=categ_name).first()
        if not category:
            category = Category(categ_name)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        res = {}
        res[product.id] = {
            'name': product.name,
            'price': product.price,
            'category': product.category.name,
        }
        return json.dumps(res)

    def put(self, id):
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        categ_name = args['category']['name']
        category = Category.query.filter_by(name=categ_name).first()
        Product.query.filter_by(id=id).update({
            'name': name,
            'price': price,
            'category_id': category.id,
        })
        db.session.commit()
        product = Product.query.get_or_404(id)
        res = {}
        res[product.id] = {
            'name': product.name,
            'price': product.price,
            'category': product.category.name,
        }
        return json.dumps(res)

    def delete(self, id):
        product = Product.query.filter_by(id=id)
        product.delete()
        db.session.commit()
        return json.dumps({'response': 'Success'})


api.add_resource(
    ProductApi,
    '/api/product',
    '/api/product/<int:id>',
    '/api/product/<int:id>/<int:page>'
)

# ---------------------------------------------------
@catalog.route('/')
@template_or_json('home.html')
def hello():
    return "Hello world!"


def format_event(event):
    return {
        "description": event.description,
        "id": event.id,
        "created_at": event.created_at
    }


# create an event
@catalog.route('/events', methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)


# get all events
@catalog.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {"events": event_list}


# get single event
@catalog.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {"event": formatted_event}


# delete event
@catalog.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id {id} deleted!'


# update event
@catalog.route('/events/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description, created_at=datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}
